import json
import re
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import *
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView


def index(request):
    category_count = Category.objects.count()
    course_count = Course.objects.count()
    lesson_count = Lesson.objects.count()
    quiz_count = Quiz.objects.count()
    categories = Category.objects.all()
    courses = Course.objects.all()[:3]
    authors = Author.objects.order_by("-created_at").all()[:3]
    return render(request, "course/index.html", context={
        "category_count": category_count,
        "course_count": course_count,
        "lesson_count": lesson_count,
        "quiz_count": quiz_count,
        "categories": categories,
        "courses": courses,
        "authors": authors
    })


# Курс
class CourseSingle(DetailView):
    model = Course
    template_name = "course/singleCourse.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['course'] = Course.objects.get(slug=self.kwargs["slug"])
        context["title"] = "Курс " + context["course"].title
        return context


# Видеоурок
class LessonSingle(DetailView):
    model = Lesson
    template_name = "course/singleLesson.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['lesson'] = Lesson.objects.get(slug=self.kwargs["slug"])
        context["title"] = "Видеоурок " + context["lesson"].title
        context['lessons'] = Lesson.objects.exclude(slug=self.kwargs["slug"]).filter(
            course_id=context["lesson"].course_id, )
        return context


class AuthorSingle(ListView):
    model = Author
    template_name = "course/singleAuthor.html"
    paginate_by = 12
    context_object_name = "courses"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['author'] = Author.objects.get(slug=self.kwargs["slug"])
        context["title"] = "Автор " + context["author"].title
        return context

    def get_queryset(self):
        return Author.objects.get(slug=self.kwargs["slug"]).courses.all()


class CoursesAll(ListView):
    model = Course
    template_name = "course/courseAll.html"
    context_object_name = "courses"
    paginate_by = 10
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories_request"] = list(map(int, self.request.GET.getlist("categories")))
        context["authors_request"] = list(map(int, self.request.GET.getlist("authors")))
        context["languages_request"] = list(map(int, self.request.GET.getlist("languages")))
        return context

    def get_queryset(self):
        courses = Course.objects.all()
        if "search" in self.request.GET:
            courses = courses.filter(title__icontains=self.request.GET["search"])
        if len(self.request.GET.getlist('categories')) != 0:
            courses = courses.filter(category_id__in=self.request.GET.getlist('categories'))
        if len(self.request.GET.getlist('authors')) != 0:
            courses = courses.filter(authors__id__in=self.request.GET.getlist('authors')).distinct()
        if len(self.request.GET.getlist('languages')) != 0:
            courses = courses.filter(language_id__in=self.request.GET.getlist('languages'))
        return courses
