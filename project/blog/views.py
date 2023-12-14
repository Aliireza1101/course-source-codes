from django.shortcuts import render
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
    return HttpResponse("Developing ...")
