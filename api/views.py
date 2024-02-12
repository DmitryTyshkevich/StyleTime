from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from api.serializers import ProductSerializer, ManufactureSerializer
from shop.models import Product, Manufacture


class ManufactureViewSet(viewsets.ModelViewSet):
    queryset = Manufacture.objects.all()
    serializer_class = ManufactureSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    @action(methods=['get'], detail=False)
    def category_casio(self, request):
        queryset = Product.objects.filter(manufacture__brand="Casio")
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)
    


