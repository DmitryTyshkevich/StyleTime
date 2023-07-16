from django.core.paginator import Paginator
from django.shortcuts import render
from shop.models import Product, Features, Manufacture
from cart.forms import CartAddProductFormV1, CartAddProductFormV2


def pagination(request, products):
    """ Для пагинации """
    num = 16
    paginator = Paginator(products, num)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return page_obj


def products_all(request):
    products = Product.objects.all()
    cart_product_form = CartAddProductFormV2()

    price = request.GET.get('sort_price')
    type_mechanism = request.GET.getlist('type')
    case_material = request.GET.getlist('case_material')
    bracelet = request.GET.getlist('bracelet_material')
    glass = request.GET.getlist('glass')

    if not type_mechanism and not bracelet and not glass \
            and not case_material and not price:

        page_obj = pagination(request, products)
        return render(
            request, 'shop/products_all.html',
            {
                'products': page_obj,
                'cart_product_form': cart_product_form
            }
        )
    elif not type_mechanism and not bracelet and not glass \
            and not case_material:
        products = products.order_by(price)

        # page_obj = pagination(request, products)
        return render(
            request, 'shop/products_all.html',
            {
                'products': products,
                'cart_product_form': cart_product_form
            }
        )

    else:
        features = Features.objects.filter(type__in=type_mechanism) \
            | Features.objects.filter(case_material__in=case_material) \
            | Features.objects.filter(bracelet_material__in=bracelet) \
            | Features.objects.filter(glass__in=glass)
        product_ids = features.values_list(
            'product',
            flat=True
        )  # Получить список идентификаторов связанных объектов Product
        all_products = products.filter(
            id__in=product_ids
        ).order_by(price)  # Получить все объекты Product по идентификаторам
        # page_obj = pagination(request, all_products)
        return render(
            request, 'shop/products_all.html',
            {
                'products': all_products, 'cart_product_form': cart_product_form
            }
        )


def catalogue(request, producer):
    products = Product.objects.filter(model__startswith=producer)
    brand = Manufacture.objects.get(brand=producer)
    cart_product_form = CartAddProductFormV2()

    price = request.GET.get('sort_price')
    type_mechanism = request.GET.getlist('type')
    case_material = request.GET.getlist('case_material')
    bracelet = request.GET.getlist('bracelet_material')
    glass = request.GET.getlist('glass')

    if not type_mechanism and not bracelet and not glass \
            and not case_material and not price:
        page_obj = pagination(request, products)
        return render(
            request, 'shop/catalogue.html',
            {
                'products': page_obj,
                'brand': brand,
                'cart_product_form': cart_product_form
            }
        )
    elif not type_mechanism and not bracelet and not glass \
            and not case_material:
        products = products.order_by(price)
        # page_obj = pagination(request, products)
        return render(request, 'shop/catalogue.html',
                      {
                          'products': products,
                          'brand': brand,
                          'cart_product_form': cart_product_form
                      }
                      )
    else:
        features = (Features.objects.filter(type__in=type_mechanism)
                    | Features.objects.filter(case_material__in=case_material)
                    | Features.objects.filter(bracelet_material__in=bracelet)
                    | Features.objects.filter(glass__in=glass)) \
            & Features.objects.filter(product__in=products)
        product_ids = features.values_list('product', flat=True)
        all_products = products.filter(id__in=product_ids).order_by(price)
        # page_obj = pagination(request, all_products)

        return render(
            request, 'shop/catalogue.html',
            {
                'products': all_products,
                'brand': brand,
                'cart_product_form': cart_product_form
            }
        )


def watch(request, producer, pk):
    cart_product_form = CartAddProductFormV1()
    product = Product.objects.get(pk=pk)
    features = Features.objects.get(product=pk)
    return render(
        request, 'shop/watch.html',
        {
            'product': product,
            'features': features,
            'cart_product_form': cart_product_form
        }
    )
