from django import forms


class Aform(forms.Form):
    first_name = forms.CharField()
    last_name= forms.CharField()
    email = forms.EmailField()
