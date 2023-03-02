import uuid

from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from loguru import logger

nb = dict(null=True, blank=True)


class GetOrNoneManager(models.Manager):
    """returns none if object doesn't exist else model instance"""

    def get_or_none(self, **kwargs):
        try:
            return self.get(**kwargs)
        except ObjectDoesNotExist as e:
            logger.warning(e)
            return None


class BaseModel(models.Model):
    class Meta:
        abstract = True
        ordering = ('-created_at',)

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField('Дата создания', auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField('Дата изменения', auto_now=True)
    objects = GetOrNoneManager()

    def str(self):
        return self.id.hex
