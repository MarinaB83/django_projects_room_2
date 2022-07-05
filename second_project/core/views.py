from django.shortcuts import HttpResponse
import random


def hello(request):
    return HttpResponse("<h1>Hello Django world </h1>")


def present(request):
    num = random.randint(1, 5)
    html_code = f"<h{num}> Name:Marina Surname:Bokrador </h{num}>"
    return HttpResponse(html_code)
