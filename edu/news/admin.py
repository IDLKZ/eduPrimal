from django.contrib import admin
from news.models import *
from .forms import *
# Register your models here.

class CategoryNewsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ("title",)

class NewsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ("title","category","author","status","published")
    form = NewsAdminForm



admin.site.register(CategoryNews,CategoryNewsAdmin)
admin.site.register(News,NewsAdmin)

