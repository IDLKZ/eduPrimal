from django.contrib import admin
from django.forms import forms
from .forms import *
from .models import *


# Register your models here.

class AuthorAdmin(admin.ModelAdmin):
    search_fields = ("title","description")
    list_display = ("title","get_image","status","created_at","updated_at")
    readonly_fields = ('get_image',)
    prepopulated_fields = {'slug': ('title',)}
    save_as = True
    form = AuthorAdminForm


class LanguageAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    save_as = True
    search_fields = ("title",)


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    form = CategoryAdminForm
    search_fields = ("title","status","description")
    list_display = ("title", "get_image","status","created_at", "updated_at",)
    readonly_fields = ("get_image",)


class CourseAdmin(admin.ModelAdmin):
    model = Course
    prepopulated_fields = {'slug': ('title',)}
    list_display = ("title","get_image","language","category")
    form = CourseAdminForm
    readonly_fields = ['created_at']

class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}



class LessonAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    save_as = True
    form = LessonAdminForm
    list_display = ("title",'subtitle',"course")

class QuizAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}



admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag,TagAdmin)
admin.site.register(Language, LanguageAdmin)
admin.site.register(Author,AuthorAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson,LessonAdmin)
admin.site.register(Quiz,QuizAdmin)
admin.site.register(Question)
