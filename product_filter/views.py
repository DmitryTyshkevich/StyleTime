from django.shortcuts import render

from shop.models import *


def product_filter(request):

    price = request.GET.get('sort_price')
    type_mechanism = request.GET.getlist('type')
    case_material = request.GET.getlist('case_material')
    bracelet = request.GET.getlist('bracelet_material')
    glass = request.GET.getlist('glass')

    if not type_mechanism and not bracelet and not glass and not case_material:
        all_products = Product.objects.all().order_by(price)
        return render(request, 'shop/products_all.html', {'products': all_products})
    else:
        products = Features.objects.filter(type__in=type_mechanism) | Features.objects.filter(
            case_material__in=case_material) | Features.objects.filter(
            bracelet_material__in=bracelet) | Features.objects.filter(glass__in=glass)
        product_ids = products.values_list('product',
                                           flat=True)  # Получить список идентификаторов связанных объектов Product
        all_products = Product.objects.filter(id__in=product_ids).order_by(
            price)  # Получить все объекты Product по идентификаторам

        return render(request, 'shop/products_all.html', {'products': all_products})
