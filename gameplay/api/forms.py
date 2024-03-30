from django import forms

class user_form(forms.Form):
    comment = forms.CharField(max_length=10)