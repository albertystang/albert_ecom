from django.shortcuts import render, get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from store.models import Product
from category.models import Category


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
        paginator = Paginator(products, 3)
        page = request.GET.get('page')
        paged_products = paginator.get_page(page)        
    else:
        products = Product.objects.all().filter(is_available=True).order_by('id')
        paginator = Paginator(products, 3)
        page = request.GET.get('page')
        paged_products = paginator.get_page(page)
    product_count = products.count()
    context = {'category': category, 'products': paged_products, 'product_count': product_count}
    return render(request, 'store/store.html', context)


def product_detail(request, cat_slug, prod_slug):
    product = Product.objects.get(category__slug=cat_slug, slug=prod_slug)
    context = {
        'product': product,        
    }
    return render(request, 'store/product_detail.html', context)