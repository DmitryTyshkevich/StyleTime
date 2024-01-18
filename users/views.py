from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, ProfileForm
from django.contrib.auth.decorators import login_required
from orders.models import Order, OrderItem
from .models import Profile
import os


def register(request):
    """Представление для регистрации пользователя"""
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user)
            username = form.cleaned_data.get('username')
            messages.success(
                request, f'Создан аккаунт {username}!')
            return redirect('users:login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
# для обеспечения ограничение доступа к профилям для
# незарегистрированных пользователей
def profile(request, username):
    """Представление для личного кабинета"""
    orders = Order.objects.filter(email=request.user.email)
    order_items = OrderItem.objects.filter(order__in=orders)
    if request.user.profile.image:
        path = f'media/{request.user.profile.image}'
    all_order_data = {}

    for item in order_items:
        # Формируем словарь с историей заказов
        all_order_data[str(item)] = all_order_data.get(str(item), [])
        all_order_data[str(item)].append(
            {
                item.product.model: {
                    'price': str(item.price),
                    'quantity': item.quantity

                }
            }
        )

    all_order_data = dict(reversed(all_order_data.items()))

    if request.method == 'POST':
        # Изменяем изображение пользователя
        if request.user.profile.image:
            os.remove(path)
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('users:profile', username=username)
    else:
        form = ProfileForm()
        return render(
            request, 'users/profile.html',
            {
                'all_order_data': all_order_data,
                'form': form
            }
        )
