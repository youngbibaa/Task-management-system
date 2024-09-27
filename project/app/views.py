from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, ProjectCreationForm, ProjectChangeForm, TaskCreationForm, TaskChangeForm
from .models import Project, Task


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

@login_required
def project_tasks(request, pk):
    project = get_object_or_404(Project, pk=pk)
    tasks = Task.objects.filter(project_name=project)
    return render(request, "app/project_tasks.html", {"project": project, "tasks": tasks})

@login_required
def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, "app/task_detail.html", {"task": task})

@login_required
def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)  
    project_pk = task.project_name.pk  
    task.delete()
    return redirect("project_tasks", pk=project_pk) 

@login_required
def change_task(request, pk):
    task = get_object_or_404(Task, pk=pk)

    if request.method == "POST":
        form = TaskChangeForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("project_tasks", pk=task.project_name.pk)  
    else:
        form = TaskChangeForm(instance=task)

    return render(request, "app/change_task.html", {"form": form})


@login_required
def create_task(request, pk):
    project = get_object_or_404(Project, pk=pk)

    if request.method == "POST":
        form = TaskCreationForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.project_name = project  
            task.save()  
            return redirect("project_tasks", pk=project.pk)
        else:
            print(form.errors)
    else:
        form = TaskCreationForm()

    return render(request, "app/create_task.html", {"form": form})

from django.http import JsonResponse
from django.views.decorators.cache import cache_page
from django.core.cache import cache

# Используем cache_page
@cache_page(60 * 15)  # кэшируем на 15 минут
def fibonacci_view(request, n):
    def fibonacci(n):
        if n <= 1:
            return n
        else:
            return fibonacci(n-1) + fibonacci(n-2)

    result = fibonacci(n)
    return JsonResponse({'number': n, 'fibonacci': result})

# Используем cache напрямую
def fibonacci_view_cache(request, n):
    cache_key = f'fibonacci_{n}'
    result = cache.get(cache_key)

    if result is None:
        def fibonacci(n):
            if n <= 1:
                return n
            else:
                return fibonacci(n-1) + fibonacci(n-2)

        result = fibonacci(n)
        cache.set(cache_key, result, timeout=60*15)

    return JsonResponse({'number': n, 'fibonacci': result})
