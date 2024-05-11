from dataclasses import fields
from django import forms
from django.utils.translation import gettext_lazy as _

from subscribe.models import Subscribe

GENDER_OPTIONS = [
    ('M', 'Male'),
    ('F', 'Female'),
    ('O', 'Others'),
    
]

class SubscribeForm(forms.ModelForm):
    class Meta:
        model=Subscribe
        # To render all fields
        fields= '__all__'
        # To exclude one fields
        # exclude = ('first_name',)
        labels={
            'first_name': _('Enter Your First Name '),
            'last_name': _('Enter Your Last Name '),
            'email': _('Enter Your Email ')
        }
        helptexts={
            
        }
        error_messages = {
            'first_name': {
                'required': _('You have to fill First Name field')
            }
        }
        widgets = {
            'gender': forms.RadioSelect(choices=GENDER_OPTIONS),
        }
# def validate_comma(value):
#     if ',' in value:
#         raise forms.ValidationError('Invalid Value entered !!!')
#     return value

# def validate_char(value):
#     if value.isdecimal() :
#         raise forms.ValidationError('Please Enter only characters ...')
#     return value

# class SubscribeForm(forms.Form):
#     first_name = forms.CharField(max_length=20, label='Enter your First Name ', help_text='Enter character only !!!', validators=[validate_comma, validate_char])
#     last_name = forms.CharField(max_length=20, label='Enter your Last Name ', disabled=False, validators=[validate_comma, validate_char])
#     email = forms.EmailField(max_length=100, validators=[EmailValidator(message='Please enter valid E-mail')])
#     age = forms.IntegerField(max_value=100, min_value=18)
    
#     # We can use clean_[field_name] syntax for validation purposes it specific for one field
#     def clean_first_name(self):
#         first_name = self.cleaned_data['first_name']
#         if "," in first_name:
#             raise forms.ValidationError("Enter Valid first name")
#         # We have to return what ever data we got
#         return first_name