from products.models import Product


def products_contents(request):

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return context
