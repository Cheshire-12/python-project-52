import django_filters
from django import forms
from django.utils.translation import gettext_lazy as _

from . import models


class TaskFilter(django_filters.FilterSet):
    self_tasks = django_filters.BooleanFilter(
        method='filter_self_tasks',
        widget=forms.CheckboxInput,
        label=_('My tasks only')
    )
    
    class Meta:
        model = models.Task
        fields = ['status', 'executor', 'labels']
    
    def filter_self_tasks(self, queryset, name, value):
        if value:
            return queryset.filter(author=self.request.user)  # type: ignore
        return queryset