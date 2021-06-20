from django import forms
import re

from boec.models.employeemodel.EmpAccount import EmpAccount
from boec.models.employeemodel.Employee import Employee


class EmployeeLoginForm(forms.Form):
    username = forms.CharField(label='username')
    password = forms.CharField(label='password')

    def clean_username(self):
        username = self.cleaned_data['username']
        if re.search(r'^\w+&', username):
            raise forms.ValidationError("your username has the specific character")
        account = EmpAccount.objects.get(username=username)
        if account is None:
            raise forms.ValidationError("account does not exist")
        return username

    def getEmployee(self):
        employee = Employee.objects.get(account__username=self.cleaned_data['username'])
        return employee
