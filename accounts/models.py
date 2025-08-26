from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_ADMIN = "admin"
    ROLE_USER = "user"
    ROLE_CHOICES = [(ROLE_ADMIN, "Admin"), (ROLE_USER, "User")]
    role = models.CharField(max_length=5, choices=ROLE_CHOICES, default=ROLE_USER)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.username} ({self.role})"
