from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser, AbstractBaseUser, PermissionsMixin
from phonenumber_field.modelfields import PhoneNumberField
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from django.db.models.query_utils import Q
from django.urls import reverse

from frontend.models import BaseModel

import random
import string
import os

# Utils Area Start
mix_vars = string.ascii_letters + string.digits
length = 20

        
def generate_random_number(k=10):
    rnum = "".join(random.choices(string.digits, k=k))
    return rnum
        
def get_random_id():
    while True:
        rid = generate_random_number(k=10)
        try:
            users = User.objects.filter(id=rid)
            if not users.exists():
                return rid
        except Exception as ex:
            return rid

# Utils Area End

# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    username = None
    id = models.CharField(_("id"), max_length=100, unique=True, primary_key=True, editable=False, default=get_random_id)
    email = models.EmailField(_('Email Address'), unique=True)
    name = models.CharField(_("Name"), max_length=1000, null=True, blank=True)
    phone = PhoneNumberField(_("Mobile No."),null=True, blank=True, region="IN") #as_e164

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()
    
    def save(self, *args, **kwargs):
        self.email = self.email.lower()
        try:
            if not self.name:
                split_email = self.email.split("@")
                self.name = split_email[0].capitalize()
        except Exception as ex:
            print("User Model - Save Method - Error : ", ex)
            
        
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.email)
    
    @property
    def get_admin_url(self):
        info = (self._meta.app_label, self._meta.model_name)
        return reverse('admin:%s_%s_change' % info, args=(self.pk,))

    @property
    def get_profile_url(self):
        return reverse('profile:Profile')

    @property
    def get_logout_url(self):
        return reverse("users:Logout")
    
    class Meta:
        ordering = ['-last_login']
