from django import forms
from django.contrib.auth import get_user_model

from task_manager.labels.models import Label

from .models import Task

User = get_user_model()


class TaskForm(forms.ModelForm):
    labels = forms.ModelMultipleChoiceField(
        queryset=Label.objects.all(),
        required=False,
        label=('Labels')
    )
    
    executor = forms.ModelChoiceField(
        queryset=User.objects.all(),
        required=False,
        label=('Executor'),
    )

    class Meta:
        model = Task
        fields = ['name', 'description', 'status', 'executor', 'labels']