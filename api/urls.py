from django.urls import path
from rest_framework.authtoken import views as api_views

from . import views

app_name = "api"

urlpatterns = [
    path('get-price/', views.GetBitcoinPriceView.as_view(), name="GetBitcoinPrice"),
]

urlpatterns += [
    path('token-auth/', api_views.obtain_auth_token),
]
