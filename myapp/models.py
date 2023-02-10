from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    phone_no = models.CharField(max_length=20, blank=True, null=True)
    is_mobile_verified = models.BooleanField(default=False)
    business_name = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.username



class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Country(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class State(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name    


class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE , related_name='user_products')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category_products')
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='brand_products')
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='country_products')
    state = models.ForeignKey(State, on_delete=models.CASCADE, related_name='state_products')
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='city_products')

    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title
