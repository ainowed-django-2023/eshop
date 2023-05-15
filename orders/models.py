from django.db import models
from django.contrib.auth.models import User
from catalog.models import Product

class Order(models.Model):
    code = models.CharField(max_length=100, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ForeignKey(Product, on_delete=models.CASCADE)
    count = models.IntegerField(default=1)
    datetime = models.DateTimeField(auto_now_add=True)
    notes = models.TextField(max_length=500)

    def __str__(self) -> str:
        return str(self.code)