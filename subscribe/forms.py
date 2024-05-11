from django import forms


class SubscribeForm(forms.Form):
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)
    email = forms.EmailField(max_length=100)
    age = forms.IntegerField(max_value=100, min_value=18)