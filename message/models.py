from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models. Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    seguidores = models.ManyToManyField(
        "self",
        related_name="seguido_por",
        symmetrical=False,
        blank=True,
    )

    def __str__(self):
        return self.usuario.username

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile(usuario=instance)
        user_profile.save()
        """
        A propriedade set precisa de iteravel e precisamos acessar o id
        para que o usuário "se siga" e possa ver suas próprias mensagens
        """
        user_profile.seguidores.add(instance.profile)
        user_profile.save()




