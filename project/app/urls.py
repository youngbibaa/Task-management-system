from django.urls import path
from django.contrib.auth import views as auth_views
from .views import home, register, create_project, change_project, project_detail, profile, project_list, project_delete, project_tasks, task_detail, change_task, task_delete, create_task
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', home, name="index"),
    path("profile/", profile, name="profile"),
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="app/login.html"),
        name="login",
    ),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("register/", register, name="register"),
    path("project_list/", project_list, name="project_list"),
    path("create_project/", create_project, name="create_project"),
    path("change_project/<int:pk>/", change_project, name="change_project"),
    path("project_delete/<int:pk>/", project_delete, name="project_delete"),
    path('projects/<int:pk>/', project_detail, name='project_detail'),
    path('project_tasks/<int:pk>/', project_tasks, name='project_tasks'),
    path('task_detail/<int:pk>/', task_detail, name="task_detail"),
    path("change_task/<int:pk>/", change_task, name="change_task"),
    path("task_delete/<int:pk>/", task_delete, name="task_delete"),
    path("create_task/<int:pk>/", create_task, name="create_task"),
]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
