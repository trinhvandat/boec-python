from . import views
from django.urls import path

urlpatterns = [
    path('', views.login, name='login'),
    path('sign_up/', views.sign_up, name="sign-up"),
    path('home/', views.show_home_page, name='home'),
    path('items/<int:id>', views.get_item, name='item-details'),
    path('carts/', views.get_carts, name='account-cart'),
    path('add_to_cart/<int:itemId>', views.add_to_cart, name='add-to-cart'),
    path('logout/', views.logout, name='logout'),
    path(r'create_order/(?P<item_id>\d+)/$', views.create_order, name='create-order'),
    path(r'orders/(?P<item_id>\d+)/$', views.confirm_order, name='confirm-order'),
    path(r'orders/(?P<order_id>\d+)/(?P<ship_type>\w+)/$', views.corfirm_shipment_method, name='choose-shipment-method'),
    path(r'payments_credit/(?P<shipment_id>\d+)/$', views.pay_credit, name='payment-credit-method'),
    path(r'payments_bank/(?P<shipment_id>\d+)/$', views.pay_bank, name='payment-bank-method')
]