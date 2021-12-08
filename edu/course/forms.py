from django import forms
from .models import *
from ckeditor.widgets import CKEditorWidget
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from ckeditor.fields import RichTextField


class CourseAdminForm(forms.ModelForm):
    class Meta:
        model = Course
        widgets={
            'description':CKEditorUploadingWidget,
            'advantages':CKEditorWidget,

        }
        fields = '__all__'


class AuthorAdminForm(forms.ModelForm):
    class Meta:
        model = Author
        widgets={
            'description':CKEditorUploadingWidget
        }
        fields = '__all__'


class CategoryAdminForm(forms.ModelForm):
    class Meta:
        model:Category
        widgets = {
            'description': CKEditorUploadingWidget
        }
        fields = '__all__'

class LessonAdminForm(forms.ModelForm):
    class Meta:
        model: Lesson
        widgets = {
            'description': CKEditorUploadingWidget
        }
        fields = '__all__'
