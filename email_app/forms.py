from django import forms
import re 

class ContactMeForm(forms.Form):
    first_name=forms.CharField(max_length=20)
    last_name=forms.CharField(max_length=20)
    email_id=forms.EmailField()
    phone_number=forms.IntegerField()
    subject=forms.CharField(widget=forms.Textarea)
    message=forms.CharField(widget=forms.Textarea)


    def clean_phone_number(self):
        phone_number=self.cleaned_data['phone_number']
        if len(str(phone_number))==10:
            return phone_number
        raise forms.ValidationError('Please enter valid mobile number')


        