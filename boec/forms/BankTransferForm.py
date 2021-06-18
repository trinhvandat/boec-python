from django import forms

class BankTransferForm(forms.Form):
    bankName = forms.CharField(label='Bank name')
    accountNumber = forms.CharField(label='Account number')