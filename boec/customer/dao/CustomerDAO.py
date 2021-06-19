from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from boec.forms.LoginForm import LoginForm
from boec.forms.RegistrationForms import RegistrationForm
from boec.item.model.Item import Item

def login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            customer = form.getCustomer()
            request.session['customer_name'] = customer.__getName__()
            request.session['customer_id'] = customer.id
            request.session['account_id'] = customer.account.id
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

def get_carts(request):
    accountId = request.session.get('account_id')
    items = Item.objects.all().filter(cart__account_id=accountId)
    return render(request, 'cart_account.html', {'item':items})

def logout(request):
    del request.session['account_id']
    del request.session['customer_id']
    del request.session['customer_name']
    return redirect('login')