from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpRequest, HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.decorators.http import require_GET
from django.db.models import Q
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank

from .models import Post, Ticket, Comment
from .forms import TicketForm, CommentForm, PostForm, SearchForm
from .utils import slugify


# Create your views here.
def index(request: HttpRequest): # Render template for url /blog/
    return render(request=request, template_name="blog/index.html")


def postList(request: HttpRequest): # Show list of posts
    posts = Post.published.all()

    paginator = Paginator(posts, 3)
    page_number = request.GET.get("page")

    try:
        posts = paginator.page(page_number)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    except PageNotAnInteger:
        posts = paginator.page(1)

    context = {"posts": posts}
    return render(request=request, template_name="blog/list.html", context=context)


def postDetail(request: HttpRequest, pk: int): # Show detail of a post
    post = get_object_or_404(Post.published, id=pk)
    comments = post.comments.all().filter(is_active=True)
    form = CommentForm()
    context = {"post": post, "form":form, "comments": comments}
    return render(request=request, template_name="blog/detail.html", context=context)


def createTicket(request: HttpRequest): # Create a ticket in template
    if request.method == "POST":
        form = TicketForm(request.POST)

        if form.is_valid():
            ticket = Ticket.objects.create()
            data = form.cleaned_data
            title = ticket.title = data["title"]
            message = ticket.message = data["message"]
            subject = ticket.subject = data["subject"]

            email = ticket.email = data["email"]
            phone = ticket.phone_number = data["phone_number"]
            ticket.save()

            return redirect("blog:index")
    else:
        form = TicketForm()

    context = {"form": form}
    return render(request=request, template_name="forms/ticket.html", context=context)


def addComment(request: HttpRequest, pk: int): # Create a comment for specific post in database
    form = CommentForm(request.POST)
    if request.user.is_authenticated:
        post = get_object_or_404(Post.published, id=pk)
        comment = None
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.is_active = True
            comment.save()

            context = {"form": form, "comment": comment, "post": post}
            return redirect("blog:post_detail", pk=pk)

        comments = post.comments.all().filter(is_active=True)
        context = {"post": post, "form": form, "comments":comments}
        return render(
            request=request, template_name="blog/detail.html", context=context
        )
    else:
        return HttpResponse("<h1>Please register your account first!</h1>")


def createPost(request:HttpRequest): # Create Post view
    if request.method == "POST":
        if not request.user.is_authenticated:
            return HttpResponse("Please register you account first!")
        form = PostForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_post = Post()
            new_post.title = data["title"]
            new_post.description = data["description"]
            new_post.reading_time = data["reading_time"]
            new_post.slug = slugify(data["title"])
            new_post.status = Post.Status.published # Only for now
            new_post.author = request.user
            new_post.save()

            return redirect("blog:post_detail", pk=new_post.id)
    else :
        form = PostForm()

    context = {"form":form}
    return render(request=request, template_name="forms/post.html", context=context)


@require_GET
def postSearch(request: HttpRequest):
    query = None
    result = []
    if request.GET.get("query"):
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data["query"]
            search_query = SearchQuery(query)
            search_vector = SearchVector("title", "description", weight="A")

            result = Post.published.annotate(
                    search=search_vector, rank=SearchRank(search_vector, search_query)
                ).filter(rank__gte=0.5).order_by("-rank")
            
    context = {
        'query': query,
        'result': result,
    }
    return render(request=request, template_name="blog/search.html", context=context)
