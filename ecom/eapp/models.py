from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    category_name = models.CharField(max_length=200)

    def __str__(self):
        return self.category_name


class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    product_image = models.ImageField(default='def.png'
                                      , upload_to='product_images')
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class CartItem(models.Model):
    customer = models.ForeignKey(to=User, on_delete=models.CASCADE)
    item_name = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.customer}'s cart item"

    def item_total(self):
        return self.item_name.price * self.quantity
