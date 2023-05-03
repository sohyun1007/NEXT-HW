from django.urls import path
from blog import views

app_name = "blog"

urlpatterns = [
    path("", views.home, name="home"),
    path("signup/", views.signup, name="signup"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path("create/", views.create, name="create"),
    path("detail/<int:post_pk>/", views.detail, name="detail"),
    path("update/<int:post_pk>/", views.update, name="update"),
    path("delete/<int:post_pk>/", views.delete, name="delete"),
    path("deleteComment/<int:post_pk>/<int:comment_pk>/", views.deleteComment, name="deleteComment"),
    path("all/<int:user_pk>/", views.all, name="all"),
]