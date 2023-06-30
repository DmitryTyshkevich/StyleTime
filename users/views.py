from django.shortcuts import render, redirect
from django.contrib import messages

from shop.models import Product
from .forms import UserRegisterForm, ProfileForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from orders.models import Order, OrderItem
from .models import Profile


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user)
            username = form.cleaned_data.get('username')
            messages.success(request, f'Создан аккаунт {username}!')
            return redirect('users:login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
# для обеспечения ограничение доступа к профилям для незарегистрированных пользователей
def profile(request, username):
    user = User.objects.get(username=username)
    orders = Order.objects.filter(email=user.email)
    order_items = OrderItem.objects.filter(order__in=orders)
    product = Product.objects.all()
    all_order_data = {}
    prof = Profile.objects.get(user=user)

    for item in order_items:
        all_order_data[str(item)] = all_order_data.get(str(item), [])
        all_order_data[str(item)].append({product.get(
            id=item.product_id).model: {'price': str(item.price), 'quantity': item.quantity}})

    all_order_data = dict(reversed(all_order_data.items()))

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=prof)
        if form.is_valid():
            form.save()
            return redirect('users:profile', username=user.username)
    else:
        form = ProfileForm()
        return render(request, 'users/profile.html', {'all_order_data': all_order_data, 'form': form})
