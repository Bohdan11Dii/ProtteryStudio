from django.urls import include, path
from product.views import CategoryViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register("categories", CategoryViewSet)


urlpatterns = [
    path("", include(router.urls))
]

app_name = "product"