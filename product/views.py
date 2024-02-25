from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from product.models import Category
from product.serializers import CategorySerializer
from rest_framework.views import APIView

# @api_view(["GET"])
# def category_list(request):
#     if request.method == "GET":
        
    

class CategoryList(APIView):
    def get(self, request) -> Response:
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data, status=200)
    