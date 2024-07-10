from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Category, Product, Review
from .serializers import CategorytSerializer, ProductSerializer, ReviewSerializer


#Category
@api_view(http_method_names=['GET'])
def category_list_api_view(request):
    category = Category.objects.all()
    data = CategorytSerializer(category, many=True).data
    return Response(data=data, status=status.HTTP_200_OK)


@api_view(http_method_names=['GET'])
def category_detail_api_view(request, id):
    try:
        category = Category.objects.get(id=id)
    except Category.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    data = CategorytSerializer(category, many=False).data
    return Response(data=data, status=status.HTTP_200_OK)


#Product
@api_view(http_method_names=['GET'])
def product_list_api_view(request):
    product = Product.objects.all()
    data = ProductSerializer(product, many=True).data
    return Response(data=data, status=status.HTTP_200_OK)


@api_view(http_method_names=['GET'])
def product_detail_api_view(request, id):
    try:
        product = Product.objects.get(id=id)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    data = ProductSerializer(product, many=False).data
    return Response(data=data, status=status.HTTP_200_OK)


#Review
@api_view(http_method_names=['GET'])
def review_list_api_view(request):
    review = Review.objects.all()
    data = ReviewSerializer(review, many=True).data
    return Response(data=data, status=status.HTTP_200_OK)


@api_view(http_method_names=['GET'])
def review_detail_api_view(request, id):
    try:
        review = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    data = ReviewSerializer(review, many=False).data
    return Response(data=data, status=status.HTTP_200_OK)