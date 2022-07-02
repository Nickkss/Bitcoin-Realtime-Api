from django.shortcuts import render
from django.contrib import messages
from django.views import View

# Create your views here.
class HomeView(View):
    def get(self, request):
        # messages.info(request, "Homepage")
        return render(request, 'index.html')

class ApisView(View):
    def get(self, request):
        
        current_site = request.scheme + "://" + request.META['HTTP_HOST']#{{request.scheme}}://{{request.META.HTTP_HOST}}
        context = {'current_site':current_site}
        return render(request, 'apis.html', context=context)