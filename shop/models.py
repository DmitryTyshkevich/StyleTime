from django.db import models


class Manufacture(models.Model):
    brand = models.CharField(max_length=50)
    country = models.CharField(max_length=20)
    description = models.TextField()
    image = models.ImageField(upload_to='brand_image/', default='no_image.jpg')
    image_brand = models.ImageField(upload_to='brand_image/', default='no_image.jpg')

    def __str__(self):
        return self.brand


class Product(models.Model):
    manufacture = models.ForeignKey(Manufacture, on_delete=models.CASCADE)
    model = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='product_image/')
    quantity = models.IntegerField(default=0)
    collection = models.CharField(max_length=50)
    date = models.DateField('Дата поступления')

    def __str__(self):
        return self.model


class Features(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    type = models.CharField(max_length=155)
    waterproof = models.CharField(max_length=50)
    weight = models.IntegerField()
    dimensions = models.CharField(max_length=50)
    date_display = models.CharField(max_length=50)
    dial = models.CharField('Циферблат', max_length=100)
    case_material = models.CharField(max_length=50)
    bracelet_material = models.CharField(max_length=50)
    glass = models.CharField(max_length=20)

    def __str__(self):
        return self.type








