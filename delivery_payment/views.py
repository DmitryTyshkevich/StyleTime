from django.shortcuts import render


def delivery_payment(request):
    return render(request, 'delivery_payment/delivery_payment.html')
