from django.urls import path
from django.contrib.auth.decorators import login_required

from . import views
from users.views import LoginView, LogoutView

app_name = "frontend"

urlpatterns = [
    path('', login_required(views.HomeView.as_view()), name="Home"),
    path('login/', LoginView.as_view(), name="Login"),
    path('login/', login_required(LogoutView.as_view()), name="Logout"),
    
    path('apis/', login_required(views.ApisView.as_view()), name="Apis"),
]
