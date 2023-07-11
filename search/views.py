from django.shortcuts import render, redirect
from cart.forms import CartAddProductFormV2
from shop.models import *


def search(request):
    cart_product_form = CartAddProductFormV2()
    search_text = request.GET['text']
    if search_text:
        products = Product.objects.filter(model__icontains=search_text)
        if products:
            return render(request, 'search/search_result.html',
                          {'products': products, 'cart_product_form': cart_product_form})
        else:
            return render(request, 'search/empty_result.html')

    else:
        # для перенаправления пользователя на предыдущую страницу, которую он
        # посещал. Если HTTP-заголовок запроса не существует, то пользователь
        # будет перенаправлен на корневой URL-адрес.
        return redirect(request.META.get('HTTP_REFERER', '/'))
