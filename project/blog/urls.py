from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path("", view=views.index, name="index"),
    path("posts/", view=views.postList, name="post_list"),
    path("posts/<pk>/", view=views.postDetail, name="post_detail"),
]
