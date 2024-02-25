from django.urls import path
from . import views as blog_views

app_name = "blog"

urlpatterns = [
    path("<int:post_id>/", blog_views.post, name="post"),
    path("", blog_views.blog, name="blog"),
    path("authors/", blog_views.blog_authors, name="blog_authors"),
]
