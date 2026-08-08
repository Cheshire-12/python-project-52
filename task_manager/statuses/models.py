from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
class Status(models.Model):
    name = models.CharField(
        max_length=255,
        unique=True,
        verbose_name=_('Name')
        )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('Date Created')
    )

    def __str__(self):
        return self.name