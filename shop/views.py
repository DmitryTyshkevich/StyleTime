from django.shortcuts import render
from shop.models import Product, Features, Manufacture
from cart.forms import CartAddProductFormV1, CartAddProductFormV2
from utils.utils import pagination, product_filter


def products_all(request):
    """Представление для отображения всего товара"""
    products = Product.objects.all()
    cart_product_form = CartAddProductFormV2()

    price = request.GET.get("sort_price")
    mechanism_type = request.GET.getlist("type")
    case_material = request.GET.getlist("case_material")
    bracelet = request.GET.getlist("bracelet_material")
    glass = request.GET.getlist("glass")

    # Условия для фильтрации товара
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
            "shop/products_all.html",
            {"products": page_obj, "cart_product_form": cart_product_form},
        )
    elif not mechanism_type and not bracelet and not glass and not case_material:
        products = products.order_by(price)

        page_obj = pagination(request, products)
        return render(
            request,
            "shop/products_all.html",
            {"products": page_obj, "cart_product_form": cart_product_form},
        )

    else:
        features = product_filter(mechanism_type, case_material, bracelet, glass)

        product_ids = features.values_list("product", flat=True)
        # Получить список идентификаторов связанных объектов Product
        # flat - чтобы не было кортежей с одним значением

        all_products = products.filter(id__in=product_ids).order_by(price)
        # Получить все объекты Product по идентификаторам
        page_obj = pagination(request, all_products)

        return render(
            request,
            "shop/products_all.html",
            {"products": page_obj, "cart_product_form": cart_product_form},
        )


def catalogue(request, producer):
    """Представление для отображения каталога производителя"""
    # products = Product.objects.filter(model__startswith=producer)
    brand = Manufacture.objects.get(brand=producer)
    products = brand.product_set.all()
    cart_product_form = CartAddProductFormV2()

    price = request.GET.get("sort_price")
    mechanism_type = request.GET.getlist("type")
    case_material = request.GET.getlist("case_material")
    bracelet = request.GET.getlist("bracelet_material")
    glass = request.GET.getlist("glass")

    # Условия для фильтрации товара
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
            "shop/catalogue.html",
            {
                "products": page_obj,
                "brand": brand,
                "cart_product_form": cart_product_form,
            },
        )
    elif not mechanism_type and not bracelet and not glass and not case_material:
        products = products.order_by(price)
        page_obj = pagination(request, products)
        return render(
            request,
            "shop/catalogue.html",
            {
                "products": page_obj,
                "brand": brand,
                "cart_product_form": cart_product_form,
            },
        )
    else:
        features = product_filter(
            mechanism_type, case_material, bracelet, glass, products=products
        )

        product_ids = features.values_list("product", flat=True)
        all_products = products.filter(id__in=product_ids).order_by(price)
        page_obj = pagination(request, all_products)

        return render(
            request,
            "shop/catalogue.html",
            {
                "products": page_obj,
                "brand": brand,
                "cart_product_form": cart_product_form,
            },
        )


def watch(request, producer, pk):
    """Представление для отображения сведений конкретного товара."""
    cart_product_form = CartAddProductFormV1()
    product = Product.objects.get(pk=pk)
    features = Features.objects.get(product=pk)
    return render(
        request,
        "shop/watch.html",
        {
            "product": product,
            "features": features,
            "cart_product_form": cart_product_form,
        },
    )
