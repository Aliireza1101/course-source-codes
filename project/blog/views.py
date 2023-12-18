from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpRequest, HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Post, Ticket, Comment
from .forms import TicketForm, CommentForm


# Create your views here.
def index(request: HttpRequest):
    return HttpResponse("Developing ...")


def postList(request: HttpRequest):
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


def postDetail(request: HttpRequest, pk: int):
    post = get_object_or_404(Post.published, id=pk)
    comments = post.comments.all().filter(is_active=True)
    form = CommentForm()
    context = {"post": post, "form":form, "comments": comments}
    return render(request=request, template_name="blog/detail.html", context=context)


def createTicket(request: HttpRequest):
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


def addComment(request: HttpRequest, pk: int):
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
