from django.conf import settings
from django.db import models


class Business(models.Model):
    name = models.CharField(max_length=150)

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='business'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name