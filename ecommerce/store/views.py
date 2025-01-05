from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import Category, Product
def store(request):
    all_products = Product.objects.all()
    context = {'products_list': all_products}
    return render(request, 'store/store.html', context)

def categories(request):
    all_categories = Category.objects.all()
    return {'all_categories': all_categories}

def product_detail(request, category_slug, product_slug):
    # product = get_object_or_404(Product, slug=product_slug)
    product = get_object_or_404(Product, slug=product_slug, category__slug=category_slug)
    context = {'product': product}
    return render(request, 'store/product_detail.html', context)

def category_list(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category)
    context = {'category': category, 'products': products}
    return render(request, 'store/list-category.html', context)

# def product_detail(request, category_slug, product_slug):
#     product = get_object_or_404(Product, slug=product_slug, category__slug=category_slug)
#     return render(request, 'store/product_detail.html', {'product': product})