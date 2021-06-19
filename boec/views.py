import datetime
import uuid
from datetime import date

from MySQLdb import Date
from django.core import serializers
from django.shortcuts import render

from .forms.BankTransferForm import BankTransferForm
from .forms.CreditCardForm import CreditCardForm
from .forms.EmployeeLoginForm import EmployeeLoginForm
from .forms.LoginForm import LoginForm
from .forms.RegistrationForms import RegistrationForm
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
# Create your views here.
from boec.models import Customer, Item, Cart, Account, Order, Shipment, Payment, CreditCard, BankTransfer, Employee, \
    ProcessedOrder, ProductReview, ProductReviewProcessed
from .forms.ReviewForm import ReviewForm


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
    reviews = ProductReview.objects.filter(product=item.product, status='APPROVED')
    return render(request, 'item_detail.html', {'item':item, 'reviews':reviews})

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

def confirm_order(request, item_id):
    item = Item.objects.get(id=item_id)
    total = ((100 - float(item.discount)) / 100) * float(item.price)
    customerId = request.session.get('customer_id')
    customer = Customer.objects.get(id=customerId)
    now = date.today()
    code=uuid.uuid4()
    order = Order.objects.create(customer=customer, item=item, total=total, code=code, createDate=now, status='CREATED')
    shipTotal = total * 0.05
    return render(request, 'shipment_information.html', {'order':order, 'shipTotal':shipTotal, 'customerName':order.customer.__getName__()})

def corfirm_shipment_method(request, order_id, ship_type):
    order = Order.objects.get(id=order_id)
    fee = order.total * 0.05
    status = 'CREATED'
    receiveDate = date.today()
    if ship_type == 'EXPRESS':
        receiveDate = (datetime.datetime.today() + datetime.timedelta(days=5)).date()
        print(receiveDate)
    shipment = Shipment.objects.create(order=order, fee=fee, status=status, type=ship_type, receiveDate=receiveDate)
    total = fee + order.total
    customerName = order.customer.__getName__()
    return render(request, 'payment_information.html', {'shipment':shipment, 'total':total, 'customerName':customerName})

def pay_credit(request, shipment_id):
    form = CreditCardForm()
    shipment = Shipment.objects.get(id=shipment_id)
    if request.method=='POST':
        form = CreditCardForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            code = form.cleaned_data['code']
            cardNumber = form.cleaned_data['cardNumber']
            paymentDate = datetime.date.today()
            total = shipment.order.total + shipment.fee
            paymentInfo = CreditCard.objects.create(total=total, paymentDate=paymentDate, nameOnCard=name, cardNumber=cardNumber, code=code, order=shipment.order, shipment=shipment)
            account = Account.objects.get(id=request.session['account_id'])
            Cart.objects.filter(account=account, item=shipment.order.item).delete()
            return render(request, 'order_success.html', {'paymentInfo':paymentInfo})
    return render(request, 'credit_payment.html', {'form':form, 'shipment':shipment})

def pay_bank(request, shipment_id):
    form = BankTransferForm()
    shipment = Shipment.objects.get(id=shipment_id)
    if request.method == 'POST':
        form = BankTransferForm(request.POST)
        if form.is_valid():
            bankName = form.cleaned_data['bankName']
            accountNumber = form.cleaned_data['accountNumber']
            paymentDate = datetime.date.today()
            total = shipment.order.total + shipment.fee
            paymentInfo = BankTransfer.objects.create(total=total, paymentDate=paymentDate, bankName=bankName,
                                                    accountNumber=accountNumber, order=shipment.order,
                                                    shipment=shipment)
            account = Account.objects.get(id=request.session['account_id'])
            Cart.objects.filter().delete()
            return render(request, 'order_success.html', {'paymentInfo': paymentInfo})
    return render(request, 'bank_payment.html', {'form': form, 'shipment': shipment})

# product review
def product_review(request, item_id):
    form = ReviewForm()
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            star = form.cleaned_data['stars']
            comment = form.cleaned_data['comment']
            account = Account.objects.get(id=request.session['account_id'])
            item = Item.objects.get(id=item_id)
            ProductReview.objects.create(rating=star, comment=comment, account=account, product=item.product, status='CREATED')
            return redirect('item-details', id=item_id)
    return render(request, 'product-review.html', {'form':form, 'itemId':item_id})





def cms_home(request):
    return render(request, 'cms/cms_home.html')

def cms_login(request):
    form = EmployeeLoginForm()
    if request.method == 'POST':
        form = EmployeeLoginForm(request.POST)
        if form.is_valid():
            employee = form.getEmployee()
            request.session['employee_id'] = employee.id
            return redirect('cms-home')
    return render(request, 'cms/employee_login.html', {'form': form})

def show_process_order_form(request):
    orders = Order.objects.filter(status='CREATED')
    return render(request, 'cms/order_process_form.html', {'orders':orders})

def process_order(request, order_id, status):
    employeeId = request.session['employee_id']
    employee = Employee.objects.get(id=employeeId)
    order = Order.objects.get(id=order_id)
    now = datetime.date.today()
    ProcessedOrder.objects.create(employee=employee, order=order, processDate=now, status=status)
    Order.objects.filter(id=order_id).update(status=status)
    return redirect('order-process-template')

def show_rating_form(request):
    productReview = ProductReview.objects.filter(status='CREATED')
    return render(request, 'cms/rating_process_form.html', {'reviews':productReview})

def process_review(request, product_review_id, status):
    employeeId = request.session['employee_id']
    employee = Employee.objects.get(id=employeeId)
    productReview = ProductReview.objects.get(id=product_review_id)
    now = datetime.date.today()
    ProductReviewProcessed.objects.create(productReview=productReview, status=status, employee=employee, processedDate=now)
    ProductReview.objects.filter(id=product_review_id).update(status=status)
    return redirect('rating-process-template')

def cms_logout(request):
    del request.session['employee_id']
    return redirect('cms-login')

