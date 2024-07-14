from rest_framework import serializers
from .models import Category, Product, Review


class CategorySerializer(serializers.ModelSerializer):
    products_count = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ['id', 'name', 'products_count']

    def get_products_count(self, category):
        count = category.categories.count()
        return count


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'product_category', 'description', 'price']
        depth = 1


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'review_product', 'text']
        depth = 1


class ProductReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = 'id description price'.split()


class ReviewProductSerializer(serializers.ModelSerializer):
    review_product = ProductReviewSerializer()

    class Meta:
        model = Review
        fields = ['id', 'review_product', 'text', 'stars', 'rating_stars']


