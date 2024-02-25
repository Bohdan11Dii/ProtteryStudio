from django.urls import path
from product.views import CategoryList

urlpatterns = [
    path("categories/", CategoryList.as_view(), name="category-list"),
]


app_name = "product"