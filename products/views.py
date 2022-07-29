from django.shortcuts import render, get_object_or_404
from .models import Product

# Create your views here.


def all_products(request):
    """ A view to render/return the all products/collection page, including \
        search and sorting """

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/collection.html', context)


def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)
