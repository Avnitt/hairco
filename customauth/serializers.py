from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from rest_framework import serializers
from django.utils.translation import gettext_lazy as _
from datetime import datetime, timedelta
import pytz

User = get_user_model()

class PhoneSerializer(serializers.Serializer):
    phone = serializers.CharField(
        label=_("Phone"),
        write_only=True
    )
    def validate(self, attrs):
        phone = attrs.get('phone')

        if phone:
            user = User.objects.get_or_create(phone=phone)
            #else:
            #    msg = _('Invalid Number')
            #    raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = _('Must include "Phone"')
            raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user 
        return attrs


class TokenSerializer(serializers.Serializer):
    phone = serializers.CharField(
        label=_("Phone"),
        write_only=True
    )
    otp = serializers.CharField(
        label=_("OTP"),
        style={'input_type': 'password'},
        write_only=True
    )
    token = serializers.CharField(
        label=_("Token"),
        read_only=True
    )

    def validate(self, attrs):
        phone = attrs.get('phone')
        otp = attrs.get('otp')
        if phone and otp:
            user = authenticate(request=self.context.get('request'),
                                phone=phone, password=otp)

            ist_now = datetime.now(pytz.UTC)
            
            if not user:
                msg = _('Invalid OTP')
                raise serializers.ValidationError(msg, code='authorization')
            
            if user.password_created < ist_now - timedelta(minutes=10):
                msg = _('OTP Expired')
                raise serializers.ValidationError(msg, code='authorization')
        
        if not otp:
            msg = _('Please enter OTP')
            raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user
        return attrs
