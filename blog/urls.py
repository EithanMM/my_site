from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("posts", views.posts, name="posts-page"),
    path("posts/<slug:slug>", views.single_posts, name="post-detail-page")
]
