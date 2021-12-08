from django import forms
from .models import *
from ckeditor.widgets import CKEditorWidget
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from ckeditor.fields import RichTextField


class NewsAdminForm(forms.ModelForm):
    class Meta:
        model = News
        widgets={
            'description':CKEditorUploadingWidget,
        }
        fields = '__all__'