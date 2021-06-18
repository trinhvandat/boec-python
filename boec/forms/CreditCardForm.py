import datetime

from django import forms
import re

from boec.models import CreditCard


class CreditCardForm(forms.Form):
    name = forms.CharField(label='Card name')
    cardNumber = forms.CharField(label='Card number')
    code = forms.CharField(label='Code')

    def clean_code(self):
        code = self.cleaned_data['code']
        if len(code) != 3:
            raise forms.ValidationError('Code must be have 3 characters.')
        if re.findall(r'\d}(?!\d)', code):
            raise forms.ValidationError('Code must be is digits.')
        return code
