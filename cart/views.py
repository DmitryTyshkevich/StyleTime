from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from shop.models import *
from .cart import Cart
from .forms import CartAddProductForm


@require_POST
# Мы используем декоратор require_POST, чтобы разрешить только POST запросы,
# поскольку это представление изменит данные.
def cart_add(request, pk):
    cart = Cart(request)
    product = get_object_or_404(Product, pk=pk)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
    return redirect('cart:cart_detail')


def cart_remove(request, pk):
    cart = Cart(request)
    product = get_object_or_404(Product, pk=pk)
    cart.remove(product)
    return redirect('cart:cart_detail')


def cart_detail(request):
    manufacture = Manufacture.objects.all()
    cart = Cart(request)
    return render(request, 'cart/detail.html', {'cart': cart})
