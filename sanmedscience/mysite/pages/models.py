from django.db import models

# Create your models here.
from django.db import models
from django import forms

class NameForm(forms.Form):
    URL = forms.CharField(label='URL', max_length=100)

