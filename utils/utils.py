from django.core.paginator import Paginator
from django.db.models import Q
from shop.models import Features, Product
from django.contrib.postgres.search import (
    SearchVector,
    SearchHeadline,
    SearchQuery,
    SearchRank,
)


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


def q_seqrch(query):
    """Функция поиска"""
    result = Product.objects.filter(
        Q(model__icontains=query) | Q(collection__icontains=query)
    )
    query = SearchQuery(query)
    # vector = SearchVector("model", "collection")

    # result = (
    #     Product.objects.annotate(rank=SearchRank(vector, query))
    #     .filter(rank__gt=0)
    #     .order_by("-rank")
    # )

    result = result.annotate(
        headline=SearchHeadline(
            "model",
            query,
            start_sel='<span style="background-color: yellow;">',
            stop_sel="</span>",
        )
    )
    result = result.annotate(
        bodyline=SearchHeadline(
            "collection",
            query,
            start_sel='<span style="background-color: yellow;">',
            stop_sel="</span>",
        )
    )

    return result
