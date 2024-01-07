from django.urls import path, include
from rest_framework import routers
from api.views import ProductViewSet, ManufactureViewSet

# router = routers.SimpleRouter()
router = routers.DefaultRouter()
router.register(r"product", ProductViewSet)
# router.register(r"casio", ProductCassioViewset)
router.register(r"manufacture", ManufactureViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
]
