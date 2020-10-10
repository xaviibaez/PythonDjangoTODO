# Representacion en el form del modelo
from django import forms
from django.forms import ModelForm

from .models import *

class TaskForm(forms.ModelForm):
    # Se necesita como minimo dos
    class Meta:
        model = Task
        fields = '__all__'