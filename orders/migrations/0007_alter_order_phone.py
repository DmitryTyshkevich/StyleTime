# Generated by Django 4.2.1 on 2024-01-14 14:49

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_alter_order_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='phone',
            field=models.CharField(max_length=17, validators=[django.core.validators.RegexValidator(regex='^\\+375\\s\\d{2}\\s\\d{3}-\\d{2}-\\d{2}$')], verbose_name='Телефон'),
        ),
    ]
