import datetime
import uuid
from datetime import date

from django.shortcuts import render

from boec.customer.model.Account import Account
from boec.forms.BankTransferForm import BankTransferForm
from boec.forms.CreditCardForm import CreditCardForm
from boec.order.model.BankTransfer import BankTransfer
from boec.order.model.Cart import Cart
from boec.order.model.CreditCard import CreditCard
from boec.order.model.Shipment import Shipment


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
