from django.urls import path
from .views import *

urlpatterns = [
    path("news/",MainNews.as_view(),name="news"),
    path("blogs/",MainBlog.as_view(),name="blogs"),
    path("newsSingle/<str:slug>",SingleNewsBlog.as_view(),name="singleNewsAndBlog")
]