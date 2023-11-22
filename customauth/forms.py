from django import forms
from django.core.exceptions import ValidationError
from .models import User

class GenerateForm(forms.Form):
    phone = forms.CharField(
        label=_("Phone")
    )

    def __init__(self, request=None, *args, **kwargs):
        self.request = request
        self.user_cache = None
        super().__init__(*args, **kwargs)

    def clean(self):
        phone = self.cleaned_data.get("phone")

        if phone:
            user_cache = User.objects.get(phone=context.form.phone)
            if self.user_cache is None:
                raise self.get_invalid_phone_error()
            else:
                otp = generate_otp()
                user_cache.password = make_password(otp)
                user_cache.save()
        return self.cleaned_data

    def get_user(self):
        return self.user_cache

    def get_invalid_phone_error(self):
        return ValidationError(
            "Invalid Phone",
            code="invalid_phone",
        )

class VerifyForm(form.Form):
    otp = forms.CharField(
        label=_("OTP"),
        strip=False,
        widget=forms.PasswordInput()
    )

    error_messages = {
        "invalid_otp": _("Invalid OTP"),
        "not_superuser": _("This account is not Superuser."),
    }

    def __init__(self, request=None, *args, **kwargs):
        self.request = request
        self.user = User.objects.get(id=kwargs['user'])
        super().__init__(*args, **kwargs)

    def clean(self):
        otp = self.cleaned_data.get("otp")

        if otp:
            if self.user.otp == otp:
                self.confirm_login_allowed(self.user)
            else:
                raise self.get_invalid_login_error()

        return self.cleaned_data

    def confirm_login_allowed(self, user):
        if not user.is_superuser:
            raise ValidationError(
                self.error_messages["not_superuser"],
                code="not_superuser",
            )

    def get_user(self):
        return self.user

    def get_invalid_login_error(self):
        return ValidationError(
            self.error_messages["invalid_otp"],
            code="invalid_otp",
        )
