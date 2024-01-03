from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path("", view=views.index, name="index"),
    path("posts/", view=views.postList, name="post_list"),
    path("posts/<pk>/", view=views.postDetail, name="post_detail"),
    path("create/", view=views.createPost, name="create_post"),
    path("posts/<pk>/add-comment/", view=views.addComment, name="add_comment"),
    path("posts/<pk>/delete/", view=views.postDelete, name="post_delete"),
    path("posts/<pk>/edit/", view=views.postEdit, name="post_edit"),
    path("ticket/", view=views.createTicket, name="ticket"),
    path("search/", view=views.postSearch, name="post_search"),
    path("profile/", view=views.profile, name="profile"),
]
