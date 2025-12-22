from django.urls import path
from . import views


urlpatterns = [    
    path('', views.home, name='home'),
    path('store/', views.store, name='store'),
    path('<slug:cat_slug>/', views.store, name='cat_products'),   
    path('<slug:cat_slug>/<slug:prod_slug>/', views.product_detail, name='product_detail'),   
]