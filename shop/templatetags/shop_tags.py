from django.utils.http import urlencode
from django import template


register = template.Library()

@register.simple_tag(takes_context=True)
def change_params(context, **kwargs):
    """Для сохранения фильтрации товаров при пагинации"""
    query = context['request'].GET.dict()
    query.update(kwargs)
    return urlencode(query)  # Метод urlencode используется для преобразования словаря параметров запроса в строку запроса.

