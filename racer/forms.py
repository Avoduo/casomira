from django import forms
from .models import Racer, Zavod

class PersonForm(forms.ModelForm):
    class Meta:
        model = Racer
        fields = ['firstname', 'lastname', 'sex', 'phone', 'date', 'email']
        labels = {
            'firstname': 'Jméno',
            'lastname': 'Příjmení',
            'sex': 'Pohlaví',
            'phone': 'Telefon',
            'date': 'Ročník narození',
            'email': 'E-mail',
        }
  