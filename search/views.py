from django.shortcuts import render, redirect
from shop.models import *


def search(request):
    search_text = request.GET['text']
    if search_text:
        products = Product.objects.filter(model__icontains=search_text)
        if products:
            return render(request, 'search/search_result.html', {'products': products})
        else:
            return render(request, 'search/empty_result.html')

    else:
        return redirect(request.META.get('HTTP_REFERER', '/'))
