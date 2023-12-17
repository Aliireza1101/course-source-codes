from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpRequest, HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Post, Ticket
from .forms import TicketForm


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
    context = {"post": post}
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
