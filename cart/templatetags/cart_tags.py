from django import template

from cart.cart import Cart

register = template.Library()


@register.simple_tag(takes_context=True)
def quantity_goods_cart(context):
    request = context['request']
    goods_in_cart = Cart(request)
    return f"+{len(goods_in_cart)}" if len(goods_in_cart) else ''
