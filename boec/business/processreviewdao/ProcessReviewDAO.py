from datetime import datetime

from django.shortcuts import render, redirect

from boec.models.employeemodel.Employee import Employee
from boec.models.processreviewmodel.ProductReviewProcessed import ProductReviewProcessed
from boec.models.productreviewmodel.ProductReview import ProductReview


def show_rating_form(request):
    productReview = ProductReview.objects.filter(status='CREATED')
    return render(request, 'cms/rating_process_form.html', {'reviews':productReview})

def process_review(request, product_review_id, status):
    employeeId = request.session['employee_id']
    employee = Employee.objects.get(id=employeeId)
    productReview = ProductReview.objects.get(id=product_review_id)
    now = datetime.today().date()
    ProductReviewProcessed.objects.create(productReview=productReview, status=status, employee=employee, processedDate=now)
    ProductReview.objects.filter(id=product_review_id).update(status=status)
    return redirect('rating-process-template')
