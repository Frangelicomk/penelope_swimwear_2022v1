from django.shortcuts import render
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
