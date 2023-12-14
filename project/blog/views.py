from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest, HttpResponse
from .models import Post


# Create your views here.
def index(request: HttpRequest):
    return HttpResponse("Developing ...")


def postList(request: HttpRequest):
    posts = Post.published.all()
    context = {"posts": posts}
    return render(request=request, template_name="blog/list.html", context=context)


def postDetail(request: HttpRequest, pk: int):
    post = get_object_or_404(Post.published, id=pk)
    context = {"post": post}
    return render(request=request, template_name="blog/detail.html", context=context)
