from django.contrib import admin
from .models import User, Category, Brand, Country, State, City, Product

# Register your models here.
admin.site.register(User)
admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Country)
admin.site.register(State)
admin.site.register(City)
admin.site.register(Product)