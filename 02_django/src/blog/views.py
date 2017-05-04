from django.shortcuts import render
from django.http import HttpResponse


def index(request):

    # return HttpResponse("Hello, world.")
	name = "yoonwoo!!!"
	return render(request, "index.html", {"name" : name})
# Create your views here.
