from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, ProjectCreationForm, ProjectChangeForm
from .models import Project


def home(request):
    return render(request, "app/index.html", {"user": request.user})


def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = CustomUserCreationForm()
    return render(request, "app/register.html", {"form": form})


@login_required
def profile(request):
    return render(request, "app/profile.html", {"user": request.user})


@login_required
def project_list(request):
    projects = Project.objects.filter(project_owner = request.user)
    return render(request, "app/project_list.html", {"projects": projects})


@login_required
def create_project(request):
    if request.method == "POST":
        form = ProjectCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("project_list")
        else:
            print(form.errors)  
    else:
        form = ProjectCreationForm()
    return render(request, "app/create_project.html", {"form": form})


@login_required
def change_project(request, pk):
    project = get_object_or_404(Project, pk = pk)
    if request.method == "POST":
        form = ProjectChangeForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect("project_list")
    else:
        form = ProjectChangeForm(instance=project)
    return render(request, "app/change_project.html", {"form": form})

@login_required
def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, "app/project_detail.html", {"project": project})

@login_required
def project_delete(request, pk):
    project = get_object_or_404(Project, pk=pk)
    project.delete()
    return redirect("project_list")
