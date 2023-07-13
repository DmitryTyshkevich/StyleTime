from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from shop.models import *
from .cart import Cart
from .forms import CartAddProductFormV1, CartAddProductFormV2


@require_POST
# Мы используем декоратор require_POST, чтобы разрешить только POST запросы,
# поскольку это представление изменит данные.
def cart_add(request, pk):
    cart = Cart(request)
    product = get_object_or_404(Product, pk=pk)
    # producer = product.model.split()[0]
    form = CartAddProductFormV1(request.POST) \
           or CartAddProductFormV2(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])

    # return redirect('shop:watch', producer=producer, pk=pk)
    return redirect(request.META.get('HTTP_REFERER', '/'))


def cart_remove(request, pk):
    cart = Cart(request)
    product = get_object_or_404(Product, pk=pk)
    cart.remove(product)
    return redirect('cart:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    if cart:
        return render(request, 'cart/detail.html', {'cart': cart})
    else:
        return render(request, 'cart/cart_empty.html')
