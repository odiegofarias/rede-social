from django.db import models
from django.contrib.auth.models import User


class Profile(models. Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    seguidores = models.ManyToManyField(
        "self",
        related_name="seguido_por",
        symmetrical=False,
        blank=True,
    )

