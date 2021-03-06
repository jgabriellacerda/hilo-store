from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=150)
    price = models.DecimalField(decimal_places=2, max_digits=6)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    img_file = models.ImageField(null=True, blank=True, upload_to="images/products/")
    class Meta:
        db_table = 'product'
        
    def __str__(self) -> str:
        return self.name