from django.db import models
from shop.models import Product
from django.core.validators import RegexValidator


class Order(models.Model):
    first_name = models.CharField('Имя', max_length=50)
    last_name = models.CharField("Фамилия", max_length=50)
    email = models.EmailField()
    address = models.CharField("Адрес", max_length=250)
    city = models.CharField("Город", max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    phoneNumberRegex = RegexValidator(regex=r'^\+375\s\d{2}\s\d{3}-\d{2}-\d{2}$')
    # Для валидации номера телефона
    phone = models.CharField('Телефон', max_length=17, validators=[phoneNumberRegex])
    paid = models.BooleanField(default=False)

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return f'Заказ {self.id}'


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    class Meta:
        verbose_name = 'Объект заказа'
        verbose_name_plural = 'Объекты заказа'

    def __str__(self):
        return str(self.order)
