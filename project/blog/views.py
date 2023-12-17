from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest, HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Post


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
