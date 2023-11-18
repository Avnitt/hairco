from rest_framework import authentication
from rest_framework import exceptions

from django.utils.translation import gettext_lazy as _

from datetime import datetime, timedelta
import pytz

class TokenAuthentication(authentication.TokenAuthentication):
    def authenticate_credentials(self, key):
        model = self.get_model()
        try:
            token = model.objects.select_related('user').get(key=key)
        except model.DoesNotExist:
            raise exceptions.AuthenticationFailed(_('Invalid token.'))

        if not token.user.is_active:
            raise exceptions.AuthenticationFailed(_('User inactive or deleted.'))
        
        ist_now = datetime.now(pytz.timezone("Asia/Kolkata"))

        if token.created < ist_now - timedelta(hours=24):
            raise exceptions.AuthenticationFailed('Token has expired')

        return (token.user, token)
