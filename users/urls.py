from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views

app_name = "users"

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name="Register"),
    path('login/', views.LoginView.as_view(), name="Login"),
    path('logout/', login_required(views.LogoutView.as_view()), name="Logout"),
]