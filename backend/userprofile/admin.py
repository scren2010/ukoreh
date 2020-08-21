from django.contrib import admin

# Register your models here.
from backend.userprofile.models import Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'user',]


admin.site.register(Profile, ProfileAdmin)