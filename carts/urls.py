from django.urls import path
from . import views


urlpatterns = [    
    path('', views.cart, name='cart'),      
    path('cart_minus/<int:product_id>/<int:cart_item_id>/', views.cart_minus, name='cart_minus'),
    path('cart_item_remove/<int:product_id>/<int:cart_item_id>/', views.cart_item_remove, name='cart_item_remove'),
    path('cart_add/<int:product_id>/', views.cart_add, name='cart_add'),
]