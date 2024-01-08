from django.core.paginator import Paginator
from django.db.models import Q
from shop.models import Features


def pagination(request, products):
    """Функция для пагинации"""
    num = 16
    paginator = Paginator(products, num)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return page_obj


def product_filter(mechanism_type, case_material, bracelet, glass, products=None):
    """Функция для фильтрации товаров"""
    features = (
        Features.objects.filter(
            Q(mechanism_type__in=mechanism_type)
            | Q(case_material__in=case_material)
            | Q(bracelet_material__in=bracelet)
            | Q(glass__in=glass)
        )
        if products is None
        else Features.objects.filter(
            Q(mechanism_type__in=mechanism_type)
            | Q(case_material__in=case_material)
            | Q(bracelet_material__in=bracelet)
            | Q(glass__in=glass)
        )
        & Features.objects.filter(product__in=products)
    )
    return features
