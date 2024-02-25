from django.http import HttpResponse

from django.shortcuts import render

context = {
    "tittle": "HomePAGE",
    "first_item_nav": "Home",
    "second_item_nav": "Blog",
    "third_item_nav": "Authors",
    "page_tittle_h1": "You are at the HOME PAGE",
}


def home(request):
    return render(request, "home/index.html", context)
