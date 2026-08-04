from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _


class Task(models.Model):
    name = models.CharField(
        max_length=255,
        unique=True,
        verbose_name=_('Name')
    )
    description = models.TextField(
        blank=True,
        verbose_name=_('Description')
    )
    status = models.ForeignKey(
        'statuses.Status',
        on_delete=models.PROTECT,
        related_name='tasks',
        verbose_name=_('Status')
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name='authored_tasks',
        verbose_name=_('Author')
    )
    executor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name='executed_tasks',
        blank=True,
        null=True,
        verbose_name=_('Executor')
    )
    labels = models.ManyToManyField(
        'labels.Label',
        blank=True,
        related_name='tasks',
        verbose_name=_('Labels')
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('Date Created')
    )

    def __str__(self):
        return self.name