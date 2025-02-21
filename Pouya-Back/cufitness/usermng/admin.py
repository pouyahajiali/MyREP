from django.contrib import admin

from .forms import UserRegistrationAdminForm
from .models import CustomUser

# Register your models here.
class CustomUserAdmin(admin.ModelAdmin):
    form = UserRegistrationAdminForm
    list_display = ('email', ) 
    search_fields = ('email',)  

admin.site.register(CustomUser, CustomUserAdmin)