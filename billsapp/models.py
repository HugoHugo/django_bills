from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phonenumber = models.CharField(max_length=255)


class Bill(models.Model):

    class Bill_products(models.TextChoices):
        COOLPRODUCT = 'CP', _('Cool Product')
        YAYPRODUCT = 'YP', _('Yay Product')

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.CharField(max_length=2,choices=Bill_products.choices,)
    price = models.IntegerField(min=0)
    discount = models.IntegerField(min=0,max=100, default=0)