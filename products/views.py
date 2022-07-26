from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Product
from .forms import ProductForm, ExtraImgForm
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


def edit_product(request, product_id):
    """ Edit a product in the store """
    product = get_object_or_404(Product, pk=product_id)
    extra_img_form = ExtraImgForm()
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product. \
                 Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'extra_img_form': extra_img_form,
        'product': product,
    }

    return render(request, template, context)


def add_extraimg(request, product_id):
    """ Adding extra images while editing a product as admin """
    if request.method == 'POST':
        form = ExtraImgForm(request.POST, request.FILES or None)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.extra_img = get_object_or_404(Product, pk=product_id)
            new_form.save()
            messages.success(request, 'Extra Image Added \
                 Successfully.')
            return redirect(reverse('edit_product', args=[product_id]))
        else:
            form = ExtraImgForm()

    return redirect(reverse('products', args=[product_id]))


@login_required
def add_product(request):
    """ Add a product to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save(Product)
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('products'))
        else:
            messages.error(request, 'Failed to add product. \
                 Please ensure the form is valid.')
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """ Delete a product from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))
