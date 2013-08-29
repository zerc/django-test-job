# coding: utf-8
from django import forms
# from django.forms import widgets
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        widgets = {
            'post': forms.widgets.HiddenInput(),
        }
