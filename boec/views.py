from django.core import serializers
from django.shortcuts import render

from .forms.LoginForm import LoginForm
from .forms.RegistrationForms import RegistrationForm
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
# Create your views here.
from boec.models import Customer, Item


def login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            customer = form.getCustomer()
            request.session['customer_name'] = customer.__getName__()
            request.session['customer_id'] = customer.id
            return redirect('/boec/home/')
    return render(request, 'registration/login.html', {'form':form})

def sign_up(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/boec/')
    return render(request, 'registration/sign_up.html', {'form':form})

def show_home_page(request):
    items = Item.objects.all()
    return render(request, 'home.html', {'items':items})

def get_item(request, id):
    item = Item.objects.get(id=id)
    return render(request, 'item_detail.html', {'item':item})
