from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=244)
    
    def __str__(self) -> str:
        return self.name
    
    
class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=244)
    colour = models.CharField(max_length=244)
    count = models.IntegerField()
    price = models.IntegerField()
    
    def __str__(self) -> str:
        return self.name
    

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE) 
    count = models.IntegerField()
    
    def __str__(self) -> str:
        return self.count         