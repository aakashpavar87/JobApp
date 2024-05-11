from django import forms


class SubscribeForm(forms.Form):
    first_name = forms.CharField(max_length=20, label='Enter your First Name ', help_text='Enter character only !!!')
    last_name = forms.CharField(max_length=20, label='Enter your Last Name ', disabled=False,)
    email = forms.EmailField(max_length=100)
    age = forms.IntegerField(max_value=100, min_value=18)
    
    # We can use clean_[field_name] syntax for validation purposes it specific for one field
    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']
        if "," in first_name:
            raise forms.ValidationError("Enter Valid first name")
        # We have to return what ever data we got
        return first_name