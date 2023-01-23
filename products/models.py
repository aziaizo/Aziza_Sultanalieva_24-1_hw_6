from django.db import models

# Create your models here.

class Product(models.Model):
    image=models.ImageField(null=True,blank=True)
    title=models.CharField(max_length=255)
    description= models.TextField()
    price = models.FloatField()
    year_of_release=models.IntegerField()
    created_data=models.DateField(auto_now_add=True)

class Review(models.Model):
    text=models.TextField()
    created_date=models.DateField(auto_now_add=True)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)

class Category(models.Model):
    title=models.CharField(max_length=80)
    products=models.ManyToManyField(Product,blank=True)

