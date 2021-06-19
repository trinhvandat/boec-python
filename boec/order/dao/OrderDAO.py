import uuid
from datetime import date

from django.shortcuts import render

from boec.customer.model.Customer import Customer
from boec.item.model.Item import Item
from boec.order.model.Order import Order


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