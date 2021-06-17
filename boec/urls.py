from . import views
from django.urls import path

urlpatterns = [
    path('', views.login, name='login'),
    path('sign_up/', views.sign_up, name="sign-up"),
    path('home/', views.show_home_page, name='home'),
    path('items/<int:id>', views.get_item, name='item-details')
]