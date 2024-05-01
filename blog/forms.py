from django import forms
from django.contrib.auth.forms import UserCreationForm

from blog.models import Category, Post, Comment


class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = ["title", "photo", "about"]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "about": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 4,
                }
            ),
            "category": forms.Select(attrs={"class": "form-control"}),
        }


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        exclude = ["slug"]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "content": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 4,
                }
            ),
            "category": forms.Select(attrs={"class": "form-control"}),
        }
        empty_labels = {"category": "Выберите категорию"}


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(label="Email адрес", help_text="eample@gmail.com")


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("name", "email", "body")
