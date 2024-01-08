from django.shortcuts import render, redirect
from cart.forms import CartAddProductFormV2
from shop.models import Product, Features
from utils.utils import pagination, product_filter
from django.db.models import Q


def search(request):
    """Представление для отображения товара согласна поискового запроса"""
    cart_product_form = CartAddProductFormV2()
    search_text = request.GET["text"]
    if search_text:
        products = Product.objects.filter(
            Q(model__icontains=search_text) | Q(collection__icontains=search_text)
        )
        if products:
            page_obj = pagination(request, products)
            return render(
                request,
                "search/search_result.html",
                {
                    "products": page_obj,
                    "cart_product_form": cart_product_form,
                    "search_text": search_text,
                },
            )
        else:
            return render(request, "search/empty_result.html")

    else:
        # для перенаправления пользователя на предыдущую страницу, которую он
        # посещал. Если HTTP-заголовок запроса не существует, то пользователь
        # будет перенаправлен на корневой URL-адрес.
        return redirect(request.META.get("HTTP_REFERER", "/"))


def filtered_search(request, text):
    """Представление для отображение отфильтрованного товара
    согласно поискового запроса"""
    products = Product.objects.filter(model__icontains=text)
    cart_product_form = CartAddProductFormV2()
    price = request.GET.get("sort_price")
    mechanism_type = request.GET.getlist("type")
    case_material = request.GET.getlist("case_material")
    bracelet = request.GET.getlist("bracelet_material")
    glass = request.GET.getlist("glass")

    if (
        not mechanism_type
        and not bracelet
        and not glass
        and not case_material
        and not price
    ):
        page_obj = pagination(request, products)
        return render(
            request,
            "search/search_result.html",
            {
                "products": page_obj,
                "cart_product_form": cart_product_form,
                "search_text": text,
            },
        )
    elif not mechanism_type and not bracelet and not glass and not case_material:
        products = products.order_by(price)
        page_obj = pagination(request, products)
        return render(
            request,
            "search/search_result.html",
            {
                "products": products,
                "cart_product_form": cart_product_form,
                "search_text": text,
            },
        )
    else:
        features = product_filter(
            mechanism_type, case_material, bracelet, glass, products=products
        )
        features = product_filter(mechanism_type, case_material, bracelet, glass)
        product_ids = features.values_list("product", flat=True)
        all_products = products.filter(id__in=product_ids).order_by(price)
        page_obj = pagination(request, all_products)

        return render(
            request,
            "search/search_result.html",
            {
                "products": page_obj,
                "cart_product_form": cart_product_form,
                "search_text": text,
            },
        )
