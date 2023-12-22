from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.contrib.auth.hashers import make_password
from django.utils.translation import gettext_lazy as _

from django.conf import settings

class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, phone, **extra_fields):
        if not phone:
            raise ValueError("The given phone must be set")
        user = self.model(phone=phone, **extra_fields)
        user.save(using=self._db)
        return user

    def create_user(self, phone, **extra_fields):
        return self._create_user(phone, **extra_fields)

    def create_superuser(self, phone, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('password', make_password(password))

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self._create_user(phone, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
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

    def __str__(self):
        return self.phone
