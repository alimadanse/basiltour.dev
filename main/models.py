
from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models
from accounts.models import CustomUser

# Create your models here.
class Tour(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    photo = models.ImageField(upload_to='tour_photos')
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
def validate_iranian_nat_id(value):
    if not value.isdigit() or len(value) != 10:
        raise ValidationError('Invalid Iranian national ID.')
    
    
class TourRegistration(models.Model):
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
    age = models.PositiveIntegerField(max_length=2 , null=True, blank=True) 
    nat_id = models.CharField(
        max_length=10,
        null=False,
        blank=False,
        default=None,
        validators=[validate_iranian_nat_id]
    )   
    


    