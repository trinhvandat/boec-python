from datetime import date, datetime

from django.shortcuts import render

from boec.order.model.Order import Order
from boec.order.model.Shipment import Shipment


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
