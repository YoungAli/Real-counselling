from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserEditForm

class CustomAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    edit_form = CustomUserEditForm
    model = CustomUser

admin.site.register(CustomUser, CustomAdmin)
