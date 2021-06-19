from django.shortcuts import redirect

from boec.customer.model.Account import Account
from boec.item.model.Item import Item
from boec.order.model.Cart import Cart


def add_to_cart(request, itemId):
    accountId = request.session.get('account_id')
    account = Account.objects.get(id=accountId)
    item = Item.objects.get(id=itemId)
    Cart.objects.create(item=item, account=account, total=0, quantity=0)
    return redirect('account-cart')