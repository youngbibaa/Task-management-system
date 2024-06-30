from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import EmailValidator
from django.conf import settings
from .managers import CustomUserManager


class CustomUser(AbstractUser):
    username = models.CharField(max_length=20, unique=True)
    email = models.EmailField(
        ("email address"),
        unique=True,
        validators=[
            EmailValidator,
        ],
    )
    registration_date = models.DateField(auto_now_add=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ("username", "first_name", "last_name")

    objects = CustomUserManager()

    def __str__(self):
        return self.email


class Project(models.Model):
    project_name = models.CharField(max_length=40)
    description = models.TextField()
    project_owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    creation_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.project_name


class Task(models.Model):
    STATUS_CHOICES = [
        ("created", "Создано"),
        ("in_progress", "В процессе"),
        ("completed", "Завершено"),
    ]

    project_name = models.ForeignKey(Project, on_delete=models.CASCADE)
    task_name = models.CharField(max_length=30)
    description = models.TextField()
    assigned_to = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    creation_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    deadline = models.DateTimeField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="created")

    def __str__(self):
        return self.project_name
