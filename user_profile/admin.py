from django.contrib import admin
from django.utils.html import format_html

import datetime
from . import models

# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    def created(self, instance):
        created_on = instance.created_on + datetime.timedelta(hours=5, minutes=30)
        date = created_on.date()
        time = created_on.time()
        temp = created_on.strftime("%d, %b %Y %I:%M:%S %p")
        return format_html(f"""
<span style="border-radius:0.25rem;box-shadow:2px 2px 5px rgba(0, 0, 0, 0.3);padding:5px;background-image:linear-gradient(to right, rgba(0,0,0,0.3), rgba(0, 0, 0, 0.6), darkorange);color:#fff;text-shadow:1px 1px 5px rgba(0, 0, 0, 0.8);">{temp}</span>
""")
        
    list_display = ['user', 'auth_token', 'created', 'updated_on']
    search_fields = ('user__name', 'user__email', 'user__phone')
    list_filter = ['created_on', 'updated_on']

admin.site.register(models.Profile, ProfileAdmin)
