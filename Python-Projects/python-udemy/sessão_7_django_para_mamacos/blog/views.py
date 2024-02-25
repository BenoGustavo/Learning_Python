from django.shortcuts import render
from blog.data import posts
from django.http import HttpResponse, Http404


def post(request, post_id):
    found_post = None

    for post in posts:
        if post["id"] == post_id:
            found_post = post
            break

    if found_post is None:
        raise Http404(f"Post with id {post_id} not found")

    return render(
        request,
        "blog/post.html",
        {
            "page_tittle_h1": "Good Choice!",
            "page__description": "This post about"
            + found_post["title"]
            + " is very interesting.",
            "tittle": found_post["title"],
            "first_item_nav": "Home",
            "second_item_nav": "Blog",
            "third_item_nav": "Authors",
            "post": found_post,
        },
    )


def blog(request):
    return render(
        request,
        "blog/blog.html",
        {
            "page_tittle_h1": "This is the blog page",
            "tittle": "Blog",
            "first_item_nav": "Home",
            "second_item_nav": "Blog",
            "third_item_nav": "Authors",
            "page__description": "Here you can see all the news from the lorem ipsum world.",
            "posts": posts,
        },
    )


context = {
    "first_item": "Me as me",
    "second_item": "Myself as myself",
    "third_item": "I as I",
    "tittle": "Authors of the blog",
    "first_item_nav": "Home",
    "second_item_nav": "Blog",
    "third_item_nav": "Authors",
}


def blog_authors(request):
    return render(request, "blog/blog_authors.html", context)
