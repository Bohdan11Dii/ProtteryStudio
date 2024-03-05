from django.urls import include, path
from product.views import CategoryViewSet, ColorViewSet, ProductViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register("categories", CategoryViewSet)
router.register("colors", ColorViewSet)
router.register("products", ProductViewSet)


urlpatterns = [
    path("", include(router.urls))
]

app_name = "product"