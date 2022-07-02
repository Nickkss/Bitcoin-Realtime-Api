from django.shortcuts import render, redirect
from django.contrib import messages

from .models import Token
from django.views import View

# Create your views here.

class ProfileView(View):
    def get(self, request):
        return render(request, 'profile/profile.html')
    
    def post(self, request):
        try:
            user = request.user
            auth_token = user.profile.auth_token
            auth_token.delete()
            new_auth_token, created = Token.objects.get_or_create(user=user)
            user.profile.auth_token = new_auth_token
            user.profile.save()
            messages.info(request, "Auth Token Changed !")
        except Exception as ex:
            messages.error(request, "Something Went Wrong !")
        return redirect(user.get_profile_url)