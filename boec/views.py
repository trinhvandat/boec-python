from django.core import serializers
from django.shortcuts import render

from .forms.LoginForm import LoginForm
from .forms.RegistrationForms import RegistrationForm
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
# Create your views here.
from boec.models import Customer, Item, Cart, Account


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

def get_item(request, id):
    item = Item.objects.get(id=id)
    return render(request, 'item_detail.html', {'item':item})

def get_carts(request):
    accountId = request.session.get('account_id')
    items = Item.objects.all().filter(cart__account_id=accountId)
    return render(request, 'cart_account.html', {'item':items})

def add_to_cart(request, itemId):
    accountId = request.session.get('account_id')
    account = Account.objects.get(id=accountId)
    item = Item.objects.get(id=itemId)
    Cart.objects.create(item=item, account=account, total=0, quantity=0)
    return redirect('account-cart')

def logout(request):
    del request.session['account_id']
    del request.session['customer_id']
    del request.session['customer_name']
    return redirect('login')

def create_order(request, item_id):
    item = Item.objects.get(id=item_id)
    total = ((100 - float(item.discount))/100) * float(item.price)
    return render(request, 'order_details.html', {'item':item, 'total':total})