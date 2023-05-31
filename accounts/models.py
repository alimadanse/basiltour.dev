from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator


def validate_iranian_nat_id(value):
    if not value.isdigit() or len(value) != 10:
        raise ValidationError('Invalid Iranian national ID.')


class CustomUser(AbstractUser):
    phone_regex = RegexValidator(
        regex=r'^09\d{9}$',
        message="Phone number must be entered in the format: '09xxxxxxxxx'."
    )

    phone_number = models.CharField(
        max_length=11,
        validators=[phone_regex],
        null=True,
        blank=True
    )
    
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    age = models.PositiveIntegerField(null=True, blank=True) 
    nat_id = models.CharField(
        max_length=10,
        null=False,
        blank=False,
        default=None,
        validators=[validate_iranian_nat_id]
    )
    
