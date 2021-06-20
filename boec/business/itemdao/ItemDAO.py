from django.shortcuts import render

from boec.models.itemmodel.Item import Item
from boec.models.productreviewmodel.ProductReview import ProductReview


def get_item(request, id):
    item = Item.objects.get(id=id)
    reviews = ProductReview.objects.filter(product=item.product, status='APPROVED')
    return render(request, 'item_detail.html', {'item':item, 'reviews':reviews})