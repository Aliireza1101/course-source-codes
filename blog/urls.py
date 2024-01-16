from django.urls import path
from . import views
from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    PasswordChangeView,
    PasswordChangeDoneView,
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,
)


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
    path("profile/delete-image/<pk>", view=views.imageDelete, name="image_delete"),

    path("login/", view=LoginView.as_view(), name="login"),
    path("logout/", view=LogoutView.as_view(), name="logout"),
    
    path("change-password/", view=PasswordChangeView.as_view(success_url="done"), name="change_password"),
    path("change-password/done/", view=PasswordChangeDoneView.as_view(), name="change_password_done"),
]
