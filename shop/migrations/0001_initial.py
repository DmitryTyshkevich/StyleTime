# Generated by Django 4.2.1 on 2023-06-03 19:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Manufacture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=20)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('image', models.ImageField(upload_to='brand_image/')),
                ('quantity', models.IntegerField(default=0)),
                ('collection', models.CharField(max_length=50)),
                ('date', models.DateField(verbose_name='Дата поступления')),
                ('manufacture', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.manufacture')),
            ],
        ),
        migrations.CreateModel(
            name='Features',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=155)),
                ('waterproof', models.CharField(max_length=50)),
                ('weight', models.IntegerField()),
                ('dimensions', models.CharField(max_length=50)),
                ('date_display', models.CharField(max_length=50)),
                ('dial', models.CharField(max_length=100, verbose_name='Циферблат')),
                ('case_material', models.CharField(max_length=50)),
                ('bracelet_material', models.CharField(max_length=50)),
                ('glass', models.CharField(max_length=20)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.product')),
            ],
        ),
    ]