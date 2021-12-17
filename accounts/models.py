from .managers import UserManager
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models

GENDER_CHOICES = (
    ('male', 'Male'),
    ('female', 'Female'))


class User(AbstractUser):
    username = None
    role = models.CharField(max_length=12, error_messages={
        'required': "Role must be provided"
    })
    gender = models.CharField(max_length=10, blank=True, null=True, default="")
    email = models.EmailField(unique=True, blank=False,
                              error_messages={
                                  'unique': "A user with that email already exists.",
                              })
    account_no=models.PositiveIntegerField(null=True,blank=True)
    ifsc=models.TextField(max_length=15)
    account_holder_name = models.CharField(max_length=25)
    address = models.TextField(max_length=50)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{8,10}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 10 digits allowed.")
    phno = models.CharField(validators=[phone_regex], max_length=17, blank=True)  # validators should be a list

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __unicode__(self):
        return self.email

    objects = UserManager()
