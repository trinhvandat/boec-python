from datetime import datetime

from django.shortcuts import render, redirect

from boec.employee.model.Employee import Employee
from boec.order.model.Order import Order
from boec.process_order.model.ProcessedOrder import ProcessedOrder


def show_process_order_form(request):
    orders = Order.objects.filter(status='CREATED')
    return render(request, 'cms/order_process_form.html', {'orders':orders})

def process_order(request, order_id, status):
    employeeId = request.session['employee_id']
    employee = Employee.objects.get(id=employeeId)
    order = Order.objects.get(id=order_id)
    now = datetime.today()
    ProcessedOrder.objects.create(employee=employee, order=order, processDate=now, status=status)
    Order.objects.filter(id=order_id).update(status=status)
    return redirect('order-process-template')