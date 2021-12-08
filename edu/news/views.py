from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import *
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
# Create your views here.

class MainNews(ListView):
    model = News
    template_name = "news/allNews.html"
    context_object_name = "news"
    paginate_by = 10

    def get_queryset(self):
        news = News.objects.filter(type=1,status=True)
        return news

class MainBlog(ListView):
    model = News
    template_name = "news/allNews.html"
    context_object_name = "news"
    paginate_by = 10

    def get_queryset(self):
        news = News.objects.filter(type=2,status=True)
        print(news)
        return news


class SingleNewsBlog(DetailView):
    model = News
    template_name = "news/singleNews.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['news'] = News.objects.get(slug=self.kwargs["slug"])
        return  context
