from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    CREATOR = "CREATOR"
    SUBSCRIBER = "SUBSCRIBER"

    ROLE_CHOICES = [
        (CREATOR, "Creator"),
        (SUBSCRIBER, "Subscriber"),
    ]
    profile_photo = models.ImageField(verbose_name="Photo de profil", upload_to="profile_photos/", blank=True, null=True)
    role = models.CharField(
        max_length=30,
        choices=ROLE_CHOICES,
        default=SUBSCRIBER,
    )
