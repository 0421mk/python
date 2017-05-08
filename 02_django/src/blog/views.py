from django.shortcuts import render
# from django.http import HttpResponse
from .models import Article

def index(request):

    # return HttpResponse("Hello, world.")
	# name = "yoonwoo!!!"
	# return render(request, "index.html", {"name" : name})
	article_list = Article.objects.all()

	# 디비만드는방법
	# Article.objects.create(
	# 	title="hello",
	# 	contents="this is test",
	# 	view_count=0
	# )
	ctx = {
		"article_list" : article_list
	}
	return render(request, "index.html", ctx)
# Create your views here.
