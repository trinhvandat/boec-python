from django.shortcuts import redirect, render

from boec.models.customermodel.Account import Account
from boec.forms.ReviewForm import ReviewForm
from boec.models.itemmodel.Item import Item
from boec.models.productreviewmodel.ProductReview import ProductReview


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