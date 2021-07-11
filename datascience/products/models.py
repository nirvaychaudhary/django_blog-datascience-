from django.db import models
from accounts.models import CustomUser
from django.utils import timezone

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=255)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{} === {}".format(self.name, self.created_date)

class Purchase(models.Model):
    Product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.PositiveBigIntegerField()
    quantity = models.PositiveBigIntegerField()
    total_price = models.PositiveBigIntegerField(blank=True)
    salesman = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now())

    def save(self, *args, **kwargs):
        self.total_price = self.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return "sold {} - {} items for {}".format(self.Product.name, self.quantity, self.total_price)
