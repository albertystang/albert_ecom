from django.urls import path
from . import views


urlpatterns = [    
    path('', views.home, name='home'),
    path('search/', views.search, name='search'),
    path('store/', views.store, name='store'),
    path('store/<slug:cat_slug>/', views.store, name='cat_products'),   
    path('store/<slug:cat_slug>/<slug:prod_slug>/', views.product_detail, name='product_detail'),    
]