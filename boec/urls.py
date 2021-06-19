from boec.customer.dao import CustomerDAO
from boec.employee.dao import EmployeeDAO
from boec.item.dao import ItemDAO
from boec.order.dao import OrderDAO
from boec.order.dao import CartDAO
from boec.order.dao import ShipmentDAO
from boec.order.dao import PaymentDAO
from boec.product_review.dao import ProductReviewDAO
from boec.process_order.dao import ProcessOrderDAO
from boec.process_review.dao import ProcessReviewDAO
from django.urls import path

urlpatterns = [
    path('', CustomerDAO.login, name='login'),
    path('sign_up/', CustomerDAO.sign_up, name="sign-up"),
    path('home/', CustomerDAO.show_home_page, name='home'),
    path('carts/', CustomerDAO.get_carts, name='account-cart'),
    path('logout/', CustomerDAO.logout, name='logout'),

    path('items/<int:id>', ItemDAO.get_item, name='item-details'),

    path('add_to_cart/<int:itemId>', CartDAO.add_to_cart, name='add-to-cart'),

    path(r'create_order/(?P<item_id>\d+)/$', OrderDAO.create_order, name='create-order'),
    path(r'orders/(?P<item_id>\d+)/$', OrderDAO.confirm_order, name='confirm-order'),

    path(r'orders/(?P<order_id>\d+)/(?P<ship_type>\w+)/$', ShipmentDAO.corfirm_shipment_method, name='choose-shipment-method'),

    path(r'payments_credit/(?P<shipment_id>\d+)/$', PaymentDAO.pay_credit, name='payment-credit-method'),
    path(r'payments_bank/(?P<shipment_id>\d+)/$', PaymentDAO.pay_bank, name='payment-bank-method'),

    path(r'product-reviews/(?P<item_id>\d+)/$', ProductReviewDAO.product_review, name='product-review'),



    path('cms/', EmployeeDAO.cms_login, name='cms-login'),
    path('cms-home/', EmployeeDAO.cms_home, name='cms-home'),
    path('cms-logout', EmployeeDAO.cms_logout, name='cms-logout'),

    path('cms-orders/', ProcessOrderDAO.show_process_order_form, name='order-process-template'),
    path('cms-ratings/', ProcessReviewDAO.show_rating_form, name='rating-process-template'),

    path(r'cms-process-order/<int:order_id>/(?P<status>\w+)/$', ProcessOrderDAO.process_order, name='process-order'),
    path(r'cms-process-review/<int:product_review_id>/(?P<status>\w+)/$', ProcessReviewDAO.process_review, name='process-review')
]