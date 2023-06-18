from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where matric_number is the unique identifiers
    for authentication instead of usernames.
    """
    def create_user(self, matric_number, password, **extra_fields):
        """
        Create and save a user with the given matric_number and password.
        """
        if not matric_number:
            raise ValueError(_("Enter a  Matric number"))

        # email = self.normalize_email(email)
        user = self.model(matric_number=matric_number, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, matric_number, password, **extra_fields):
        """
        Create and save a SuperUser with the given matric_number and password.
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))
        return self.create_user(matric_number, password, **extra_fields)

class CustomUser(AbstractUser):
    username = None
    matric_number = models.CharField(max_length=10, blank=True, null=True, unique=True)
    email = models.EmailField(_("email address"),  max_length=50, null=True, blank=True, unique=True)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = "matric_number"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.matric_number

    class Meta:
        unique_together = ['matric_number', 'email']
