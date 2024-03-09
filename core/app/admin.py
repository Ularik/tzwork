from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Recipes)
admin.site.register(Category)
admin.site.register(TypeMeal)
admin.site.register(ProductList)


