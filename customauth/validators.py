import re

from django.core import validators
from django.utils.deconstruct import deconstructible
from django.utils.translation import gettext_lazy as _

@deconstructible
class PhoneValidator(validators.RegexValidator):
    regex = r'^(?:\+91[\-\s]?)?[789]\d{9}$'
    message = _(
        "Enter a Valid Phone Number."
    )
    flags = 0


def phone_validator(phone):
    pattern = r'^(?:\+91[\-\s]?)?[789]\d{9}$'
    match = re.match(pattern, phone)
    if match and len(match.group()) == 10:
        return True
    else:
        return False
#@deconstructible
#class validate_phone(validators.RegexValidator):
#    regex = r'^\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}$'
#    message = -(
#        "Enter a Valid Phone Number."
#    )
#    flags = 0
