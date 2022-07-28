from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, 'There is nothing yet in your bag')
        return redirect(reverse('products'))
    

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_puclic_key': 'pk_test_51LJfiCD5pTpnFYApxznAF0z0Vjeu5hfr2c3Ao3GBrFvI9Sh373mW9lcujNBwh9M9vOlQOxdPZHou4Cu3VayF7kaA00xz96SKnQ',
        'client_secret': "test client secret",
    }

    return render(request, template, context)



