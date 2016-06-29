from django import forms

from .models import Transact

class TransactForm(forms.ModelForm):
    class Meta:
        model = Transact
        fields = ['account', 'category', 'person']
