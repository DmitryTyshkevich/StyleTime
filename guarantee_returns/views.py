from django.shortcuts import render


def guarantee_returns(request):
    return render(request, 'guarantee_returns/guarantee_returns.html')
