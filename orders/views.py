from django.shortcuts import render, redirect
from .models import OrderItem, Order
from .forms import OrderCreateForm, OrderCreateAuthUser
from cart.cart import Cart


def order_create(request):
    cart = Cart(request)
    if not request.user.is_authenticated:
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
    else:
        if request.method == 'POST':
            form = OrderCreateAuthUser(request.POST)
            if form.is_valid():
                print(request.user.first_name)
                order = Order(
                    first_name=request.user.first_name,
                    last_name=request.user.last_name,
                    email=request.user.email,
                    address=form.cleaned_data['address'],
                    city=form.cleaned_data['city'],
                    phone=form.cleaned_data['phone']

                )
                order.save()
                for item in cart:
                    OrderItem.objects.create(order=order,
                                             product=item['product'],
                                             price=item['price'],
                                             quantity=item['quantity'])
                # очистка корзины
                cart.clear()
                return redirect('orders:order_created', pk=order.id)

        else:
            form = OrderCreateAuthUser()
        return render(request, 'orders/create.html',
                      {'cart': cart, 'form': form})


def order_created(request, pk):
    return render(request, 'orders/created.html', {'id': pk})
