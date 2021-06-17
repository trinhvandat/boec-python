from django import forms
import re

from boec.models import Account, Customer


class LoginForm(forms.Form):
    username = forms.CharField(label='username')
    password = forms.CharField(label='password')

    def clean_username(self):
        username = self.cleaned_data['username']
        if re.search(r'^\w+&', username):
            raise forms.ValidationError("your username has the specific character")
        account = Account.objects.get(username=username)
        if account is None:
            raise forms.ValidationError("account does not exist")
        return username

    def getCustomer(self):
        customer = Customer.objects.get(account__username=self.cleaned_data['username'])
        return customer