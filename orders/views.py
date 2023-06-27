from django.shortcuts import render, redirect
from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart


def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])
            # очистка корзины
            cart.clear()
            return redirect('orders:order_created', pk=order.id)
    else:
        form = OrderCreateForm()
    return render(request, 'orders/create.html',
                  {'cart': cart, 'form': form})


def order_created(request, pk):
    return render(request, 'orders/created.html', {'id': pk})
