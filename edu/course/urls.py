from django.urls import path
from .views import *

urlpatterns = [
    path("",index),
    path("course/<str:slug>",CourseSingle.as_view(),name="singleCourse"),
    path("lesson/<str:slug>",LessonSingle.as_view(),name="singleLesson"),
    path("author/<str:slug>",AuthorSingle.as_view(),name="singleAuthor"),
    path("courses/",CoursesAll.as_view(),name="allCourses"),
]