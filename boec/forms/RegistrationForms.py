from django import forms
import re

from boec.models import Customer, Account, FullName, Address, Cart


class RegistrationForm(forms.Form):
    firstName = forms.CharField(label='firstName')
    midName = forms.CharField(label="midName")
    lastName = forms.CharField(label='lastName')
    email = forms.CharField(label='email')
    phoneNumber = forms.CharField(label='phoneNumber')
    numberHouse = forms.CharField(label='numberHouse')
    street = forms.CharField(label='street')
    district = forms.CharField(label='district')
    city = forms.CharField(label='city')
    username = forms.CharField(label='username')
    password1 = forms.CharField(label='password', widget=forms.PasswordInput())
    password2 = forms.CharField(label='repeatPassword', widget=forms.PasswordInput())

    def clean_password2(self):
        if 'password1' in self.cleaned_data:
            password1 = self.cleaned_data['password1']
            password2 = self.cleaned_data['password2']
            if password1 == password2 and password1:
                return password2
        raise forms.ValidationError("un valid password")

    def clean_username(self):
        username = self.cleaned_data['username']
        if re.search(r'^\w+&', username):
            raise forms.ValidationError("your username has the specific character")
        try:
            Account.objects.get(username=username)
        except Account.DoesNotExist:
            return username
        raise forms.ValidationError("account exist")

    def save(self):
        fullname = FullName.objects.create(firstName=self.cleaned_data['firstName'], midName=self.cleaned_data['midName'], lastName=self.cleaned_data['lastName'])
        address = Address.objects.create(numberHouse=self.cleaned_data['numberHouse'], street=self.cleaned_data['street'], district=self.cleaned_data['district'], city=self.cleaned_data['city'])
        account = Account.objects.create(username=self.cleaned_data['username'], password=self.cleaned_data['password1'])
        Customer.objects.create(fullName=fullname, account=account, address=address, email=self.cleaned_data['email'], phoneNumber=self.cleaned_data['phoneNumber'])
        Cart.objects.create(quantity=0, total=1, account=account)