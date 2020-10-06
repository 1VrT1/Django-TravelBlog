from django import forms
from .models import *
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class PostsForm(forms.ModelForm):

    class Meta:
        model = Posts
        fields = ('country', 'city', 'title', 'category', 'poster', 'is_public', 'body')
        widgets = {
            "country": forms.TextInput(attrs={"class": "form-control"}),
            "city": forms.TextInput(attrs={"class": "form-control"}),
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "category": forms.Select(attrs={"class": "form-control"}),
            "is_public": forms.CheckboxInput(attrs={"type": "checkbox", "class": "custom-control-input",
                                                    "id": "check"}),
            "body": CKEditorUploadingWidget
        }
