from dataclasses import field
from django import forms
from .models import TodoApp


class TodoAppForm(forms.Model):
    class Meta:
        model = TodoApp
        field = [ "title", "description"]
        