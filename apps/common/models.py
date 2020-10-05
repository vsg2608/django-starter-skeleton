from django.db import models
from django.utils import timezone


class BaseModel(models.Model):
    created_at = models.DateTimeField(verbose_name='Created At',db_index=True, default=timezone.now)
    updated_at = models.DateTimeField(verbose_name='Updated At',auto_now=True)

    class Meta:
        abstract = True
