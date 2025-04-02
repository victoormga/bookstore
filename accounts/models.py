from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

class CustomUser(AbstractUser):  # Mejor usar AbstractUser
    uid = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=30, unique=True)

    USERNAME_FIELD = "email"  # Usar email en lugar de uid
    REQUIRED_FIELDS = ["username"]  # Campos requeridos al crear usuario