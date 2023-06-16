from django.shortcuts import render
from .models import *
from cart.forms import CartAddProductForm


# def index(request):
#     manufacture = Manufacture.objects.all()
#     return render(request, 'shop/index.html', {'manufacture': manufacture})


def catalogue(request, producer):
    products = Product.objects.filter(model__startswith=producer)
    brand = Manufacture.objects.get(brand=producer)
    return render(request, 'shop/catalogue.html', {'products': products, 'brand': brand})


def watch(request, producer, pk):
    cart_product_form = CartAddProductForm()
    product = Product.objects.get(pk=pk)
    features = Features.objects.get(product=pk)
    return render(request, 'shop/watch.html', {'product': product, 'features': features,
                                               'cart_product_form': cart_product_form})

