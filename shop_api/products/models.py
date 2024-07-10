from django.db import models

# Create your models here.

class Category(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Product(models.Model):
    product_category = models.ForeignKey(Category, on_delete=models.CASCADE
                                )
    id = models.IntegerField(primary_key=True)
    description = models.TextField()
    price = models.IntegerField(default=100)

    def __str__(self):
        return f"{self.description}: {self.price}"


class Review(models.Model):
    review_product = models.ForeignKey(Product, on_delete=models.CASCADE
                                       )
    id = models.IntegerField(primary_key=True)
    text = models.TextField()

    def __str__(self):
        return self.text

