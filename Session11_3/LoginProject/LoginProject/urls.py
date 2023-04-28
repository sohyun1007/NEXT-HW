"""
URL configuration for LoginProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from LoginApp import views
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path("", views.home, name="home"),
    path("create/", views.create, name="create"),
    path("project/", views.project, name="project"),
    path("signup/", views.signup, name="signup"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path("datail/<int:project_id>/", views.detailProject, name="detailProject"),
    path("delete/<int:project_id>/", views.deleteProject, name="deleteProject"),
    path("delete/<int:project_id>/<comment_id>/", views.deleteComment, name="deleteComment"),
    path("edit/<int:project_id>/", views.edit, name="edit"),
]
