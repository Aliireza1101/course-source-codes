from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


# Create your views here.
def index(request: HttpRequest):
    return HttpResponse("Developing ...")


def postList(request: HttpRequest):
    return HttpResponse("Developing ...")


def postDetail(request: HttpRequest, pk: int):
    return HttpResponse("Developing ...")
