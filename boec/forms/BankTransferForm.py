from django import forms
import re

class BankTransfer(forms.Form):
    bankName = forms.CharField(label='Bank name')
    accountNumber = forms.CharField(label='Account number')

    def clean_code(self):
        accountNumber = self.cleaned_data['accountNumber']
        if re.findall(r'\d}(?!\d)', accountNumber):
            raise forms.ValidationError('account number must be is digits.')
        return accountNumber