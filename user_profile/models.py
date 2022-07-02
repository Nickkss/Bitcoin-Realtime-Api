from django.db import models
from rest_framework.authtoken.models import Token
from django.utils.translation import ugettext_lazy as _

from users.models import User
from frontend.models import BaseModel

# Create your models here.

class Profile(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    auth_token = models.OneToOneField(Token, on_delete=models.SET_NULL, null=True, related_name="profile_auth_token")