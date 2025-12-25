from django.shortcuts import render, get_object_or_404
#from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.core.paginator import Paginator
from django.db.models import Q
from store.models import Product
from carts.models import CartItem
from category.models import Category
from carts.views import _cart_id


def home(request):
    products =Product.objects.filter(is_available=True)
    context = {'products': products}
    return render(request, 'store/home.html', context)


def store(request, cat_slug=None):
    category = None
    products = None
    if cat_slug != None:
        category = get_object_or_404(Category, slug=cat_slug)
        products = Product.objects.filter(category=category, is_available=True)                
    else:
        products = Product.objects.all().filter(is_available=True).order_by('id')
    paginator = Paginator(products, 6)
    page = request.GET.get('page')
    paged_products = paginator.get_page(page)
    product_count = products.count()    
    context = {'category': category, 'products': paged_products, 'product_count': product_count}
    return render(request, 'store/store.html', context)


def product_detail(request, cat_slug, prod_slug):
    try:
        product = Product.objects.get(category__slug=cat_slug, slug=prod_slug)
        in_cart = CartItem.objects.filter(cart__cart_id=_cart_id(request), product=product).exists()
    except:
        pass
    context = {
        'product': product,
        'in_cart': in_cart  
    }
    return render(request, 'store/product_detail.html', context)


def search(request):
    if 'query' in request.GET:
        query = request.GET['query']
        if query:
            products = Product.objects.order_by('-created_date').filter(Q(description__icontains=query) | Q(product_name__icontains=query))
            product_count = products.count()
    context = {
        'products': products,
        'product_count': product_count,
    }
    return render(request, 'store/store.html', context)    