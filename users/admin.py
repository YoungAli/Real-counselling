from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ("matric_number", "is_staff", "is_active",)
    list_filter = ("matric_number", "is_staff", "is_active",)
    fieldsets = (
        (None, {"fields": ("matric_number", "password")}),
        ("Permissions", {"fields": ("is_staff", "is_active", "groups", "user_permissions")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "matric_number", "password1", "password2", "is_staff",
                "is_active", "groups", "user_permissions"
            )}
        ),
    )
    search_fields = ("matric_number",)
    ordering = ("matric_number",)


admin.site.register(CustomUser, CustomUserAdmin)