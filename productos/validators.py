import re
from django.core.exceptions import ValidationError

def validate_only_letters(value):
    if not re.match("^[a-zA-ZÀ-ÿ\u00f1\u00d1\s]+$", value):
        raise ValidationError('El nombre solo debe contener letras.')
