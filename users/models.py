from phonenumber_field.modelfields import PhoneNumberField
from django.db import models

# Create your models here.

from django.contrib.auth.models import (
    AbstractUser, PermissionsMixin, BaseUserManager,
)


class UserManager(BaseUserManager):

    def _create_user(self, email, password, **extra_fields):
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, password, **extra_fields)

    def create_user(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):

    class Roles(models.TextChoices):
        USER = "user"
        COMPANY = "company"
        ADMIN = "admin"
        MANAGER = "manager"

    email = models.EmailField(max_length=40, unique=True, blank=False)
    username = None
    is_verified = models.BooleanField(default=False)
    first_name = models.CharField(max_length=30, blank=False)
    last_name = models.CharField(max_length=30, blank=False)
    phone = PhoneNumberField()
    password = models.CharField(max_length=255, blank=False)
    role = models.CharField(max_length=40, choices=Roles.choices, default="user")
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['password']

    def __str__(self):
        return self.email

