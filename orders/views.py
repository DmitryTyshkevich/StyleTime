from django.shortcuts import render, redirect
# from .message_sending import message_sending
from .tasks import message_sending
from .models import Order
from .forms import OrderCreateForm, OrderCreateAuthUser
from cart.cart import Cart
from smtplib import SMTPDataError

from utils.utils import creating_order


def order_create(request):
    """Представление для создания заказа"""
    cart = Cart(request)
    # Получаем текущую корзину
    if not request.user.is_authenticated:
        # Записываем данные заказа для неавторизованного покупателя
        if request.method == 'POST':
            form = OrderCreateForm(request.POST)
            if cart:
                if form.is_valid():
                    order = form.save()
                    creating_order(cart, order)
                    # очистка корзины
                    cart.clear()
                    try:
                        # message_sending(order)
                        message_sending.delay(order.id)
                        return redirect('orders:order_created', pk=order.id)
                    except SMTPDataError:
                        return redirect('orders:order_created', pk=order.id)
                    # Отправка сообщения на email

            else:
                return render(request, 'cart/cart_empty.html')

        else:
            form = OrderCreateForm()
        return render(request, 'orders/create.html',
                      {'cart': cart, 'form': form})
    else:
        # Записываем данные заказа для авторизованного покупателя
        if request.method == 'POST':
            form = OrderCreateAuthUser(request.POST)
            if cart:
                if form.is_valid():
                    order = Order(
                        first_name=request.user.first_name,
                        last_name=request.user.last_name,
                        email=request.user.email,
                        address=form.cleaned_data['address'],
                        city=form.cleaned_data['city'],
                        phone=form.cleaned_data['phone']

                    )
                    order.save()
                    creating_order(cart, order)
                    # очистка корзины
                    cart.clear()
                    try:
                        # message_sending(order)
                        message_sending.delay(order.id)
                        return redirect('orders:order_created', pk=order.id)
                    except SMTPDataError:
                        return redirect('orders:order_created', pk=order.id)
                    # Отправка сообщения на email
            else:
                return render(request, 'cart/cart_empty.html')

        else:
            form = OrderCreateAuthUser()
        return render(request, 'orders/create.html',
                      {'cart': cart, 'form': form})


def order_created(request, pk):
    """Представление для отображения страницы
    после успешного оформления заказа"""
    return render(request, 'orders/created.html', {'id': pk})
