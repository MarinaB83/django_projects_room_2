from django.shortcuts import HttpResponse

# Create your views here.


def greeting(request):
    print(request)
    return HttpResponse("HELLO FROM PYTHON GROUP")

