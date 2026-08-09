from django import forms
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

from task_manager.labels.models import Label

from .models import Task

User = get_user_model()


class UserModelChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.get_full_name() or obj.username


class TaskForm(forms.ModelForm):
    labels = forms.ModelMultipleChoiceField(
        queryset=Label.objects.all(),
        required=False,
        label=_('Labels')
    )
    
    executor = UserModelChoiceField(
        queryset=User.objects.all(),
        required=False,
        label=_('Executor'),
    )

    class Meta:
        model = Task
        fields = ['name', 'description', 'status', 'executor', 'labels']