from django.db import models

# Create your models here.
class Cart(models.Model):
    chosen_productname = models.CharField(max_length=100)
    chosen_price = models.IntegerField()
    def __str__(self):
        return self.chosen_productname
    
class Payment(models.Model):
    first_name =  models.CharField(max_length=100)
    last_name =  models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    card_number = models.BigIntegerField()
    def __str__(self):
        return self.fname
    