import random
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

# function based view
def home(request):
    num     = None
    num1    = random.randint(0, 10000)
    num2    = random.randint(0, 10000)
    some_list = [random.randint(0, 10000), num1, num2]

    condition_bool_item = True
    if condition_bool_item:
        num     = random.randint(0, 10000)

    context = {"html_var": "context",
               "num": num,
               "some_list": some_list
    }

    return render(request, "home.html", context)


def about(request):
    context = {}
    return render(request, "about.html", context)


def contact(request):
    context = {}
    return render(request, "contact.html", context)