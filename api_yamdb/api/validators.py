import re
from datetime import datetime

from django.core.exceptions import ValidationError


def get_year_now():
    return datetime.now().year


def username_validator(value):
    unmatched = re.sub(r"[\w.@+-]", "", value)
    if value == "me":
        raise ValidationError('Имя пользователя "me" использовать нельзя!')
    if value in unmatched:
        raise ValidationError(
            f"Имя пользователя не должно содержать {unmatched}"
        )
    return value
