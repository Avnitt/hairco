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
        return self._create_user(phone, **extra_fields)

    def create_staff(self, phone, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        return self._create_user(phone, **extra_fields)

    def create_superuser(self, phone,  **extra_fields):
        extra_fields.setdefault("is_superuser", True)
        return self._create_user(phone, **extra_fields)

class User(AbstractBaseUser):
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
    is_superuser = models.BooleanField(
        _("superuser status"),
        default=False,
    )
    is_staff= models.BooleanField(
        _("staff status"),
        default=False,
    )
    date_joined = models.DateTimeField(_("date_joined"), auto_now_add=True)
    password_created = models.DateTimeField(_('password_created'), auto_now=True)
    objects = UserManager()

    USERNAME_FIELD = 'phone'

    class Meta:
        ordering = ['-date_joined']
