from django.shortcuts import render, redirect
from django.contrib import messages

from shop.models import Product
from .forms import UserRegisterForm, ProfileForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from orders.models import Order, OrderItem


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Ваш аккаунт создан: можно войти на сайт.')
            return redirect('users:login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request, username):
    image_form = ProfileForm()
    user = User.objects.get(username=username)
    orders = Order.objects.filter(email=user.email)
    order_items = OrderItem.objects.filter(order__in=orders)
    product = Product.objects.all()
    all_order_data = {}

    for item in order_items:
        all_order_data[str(item)] = all_order_data.get(str(item), [])
        all_order_data[str(item)].append({product.get(id=item.product_id).model:
                                 {'price': str(item.price), 'quantity': item.quantity}})

    all_order_data = dict(reversed(all_order_data.items()))
    return render(request, 'users/profile.html', {'all_order_data': all_order_data, 'image_form': image_form})
