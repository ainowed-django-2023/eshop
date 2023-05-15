from django.shortcuts import render
from .models import *


def index(request):
    all_products = Product.objects.all()
    all_categories = Category.objects.all()
    all_producers = Producer.objects.all()
    return render(request, 'catalog/index.html', context={
        'page_title': 'Catalog',
        'app': 'index',
        'page': 'catalog',
        'all_products': all_products,
        'all_categories': all_categories,
        'all_producers': all_producers,
    })
