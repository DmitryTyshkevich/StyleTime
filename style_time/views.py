from django.shortcuts import render

from shop.models import Manufacture


def index(request):
    manufacture = Manufacture.objects.all()
    return render(request, 'index.html', {'manufacture': manufacture})
