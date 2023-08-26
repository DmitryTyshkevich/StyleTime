from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from shop.models import *
from .cart import Cart
from .forms import CartAddProductFormV1, CartAddProductFormV2


@require_POST
# Декоратор для того, чтобы разрешить только POST запросы,
# поскольку это представление изменит данные.
def cart_add(request, pk):
    """
    Представление для добавления продуктов в корзину 
    или обновления количества для существующих продуктов
    """
    cart = Cart(request)
    product = get_object_or_404(Product, pk=pk)
    form = CartAddProductFormV1(request.POST) \
        or CartAddProductFormV2(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])

    return redirect(request.META.get('HTTP_REFERER', '/'))
    # Для перенаправления пользователя на предыдущую страницу, которую он
    # посещал. Если HTTP-заголовок запроса не существует, то пользователь
    # будет перенаправлен на корневой URL-адрес.


def cart_remove(request, pk):
    """Представление для удаления товаров из корзины"""
    cart = Cart(request)
    product = get_object_or_404(Product, pk=pk)
    cart.remove(product)
    return redirect('cart:cart_detail')


def cart_detail(request):
    """Представление для отображения корзины и ее товаров"""
    cart = Cart(request)
    if cart:
        return render(request, 'cart/detail.html', {'cart': cart})
    else:
        return render(request, 'cart/cart_empty.html')
