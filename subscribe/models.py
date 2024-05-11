from django import forms
from django.db import models
from django.core.validators import EmailValidator

def validate_comma(value):
    if ',' in value:
        raise forms.ValidationError('Invalid Value entered !!!')
    return value

def validate_char(value):
    if value.isdecimal() :
        raise forms.ValidationError('Please Enter only characters ...')
    return value

NEWSLATTER_OPTIONS = [
    ('W', 'Weekly'),
    ('M', 'Monthly')
]
GENDER_OPTIONS = [
    ('M', 'Male'),
    ('F', 'Female'),
    ('O', 'Others')
]

# Create your models here.
class Subscribe(models.Model):
    first_name = models.CharField(max_length=100, validators=[validate_char, validate_comma])
    last_name = models.CharField(max_length=100, validators=[validate_char, validate_comma])
    email = models.CharField(max_length=100, validators=[EmailValidator(message='Enter valid Email')])
    option= models.CharField(max_length=2, default='W', choices=NEWSLATTER_OPTIONS)
    gender = models.CharField(max_length=2, default='M')
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
