# from django.http import HttpResponse
from django.shortcuts import render

def home_view(request):
    # return HttpResponse("<h1>Hi Universe</h1><p>Hola Halo Hai</p>")
    value = "hello world 5"
    return render(request, 'main.html', {'key_in_the_template': value})