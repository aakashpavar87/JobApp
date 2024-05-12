from django import forms
from django.db import models

def validate_char(value):
    if value.isdecimal() :
        raise forms.ValidationError('Please Enter only characters ...')
    return value

# Create your models here.
class Uploads(models.Model):
    image = models.ImageField(upload_to='images')
    description = models.CharField(max_length=200, validators=[validate_char])
    
    def __str__(self):
        return self.description
    
class UploadFile(models.Model):
    file = models.FileField(upload_to='files')
    description = models.CharField(max_length=200, validators=[validate_char])
    
    def __str__(self):
        return self.description