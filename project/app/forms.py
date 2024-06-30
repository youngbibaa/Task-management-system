from django.contrib.auth.forms import UserCreationForm, UserChangeForm  # type: ignore
from .models import CustomUser, Project, Task
from django import forms

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = (
            "email",
            "username",
            "first_name",
            "last_name",
            "password1",
            "password2",
        )


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = (
            "email",
            "username",
            "first_name",
            "last_name",
        )


class ProjectCreationForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ("project_name", "description", "project_owner")


class ProjectChangeForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ("project_name", "description", "project_owner")


class TaskCreationForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = (
            "project_name",
            "task_name",
            "description",
            "assigned_to",
            "deadline",
            "status",
        )


class TaskChangeForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = (
            "project_name",
            "task_name",
            "description",
            "assigned_to",
            "deadline",
            "status",
        )
