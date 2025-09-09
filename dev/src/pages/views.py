from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# views handles your various webpages/websites


# creating home view
def home_view(*args, **kwargs):
    return HttpResponse("<h1>Hello World</h1>")

