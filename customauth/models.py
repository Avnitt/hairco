from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils.translation import gettext_lazy as _

from django.conf import settings

class UserManager(BaseUserManager):
    def _create_user(self, phone, **extra_fields):
        if not phone:
            raise ValueError("The given phone must be set")
        user = self.model(phone=phone, **extra_fields)
        user.save(using=self._db)
        return user

    def create_user(self, phone, **extra_fields):
        extra_fields.setdefault("role", 'client')
        return self._create_user(phone, **extra_fields)

    def create_professional(self, phone, **extra_fields):
        extra_fields.setdefault("role", 'professional')
        return self._create_user(phone, **extra_fields)

    def create_superuser(self, phone,  **extra_fields):
        extra_fields.setdefault("role", 'admin')
        return self._create_user(phone, **extra_fields)

class User(AbstractBaseUser):
    CHOICES = [
        ('admin', 'Admin'),
        ('professional', 'Professional'),
        ('client', 'Client')
    ]
    phone = models.CharField(
        _("phone"),
        max_length=10,
        unique=True,
        error_messages={
            "unique": _("A user with that username already exists."),
        }
    )
    name = models.CharField(_("name"), max_length=150)
    is_active = models.BooleanField(
        _("active"),
        default=True,
    )
    date_joined = models.DateTimeField(_("date_joined"), auto_now_add=True)
    password_created = models.DateTimeField(_('password_created'), auto_now=True)
    role = models.CharField(max_length=12,choices=CHOICES, default='client')
    objects = UserManager()

    USERNAME_FIELD = 'phone'

    class Meta:
        ordering = ['-date_joined']
