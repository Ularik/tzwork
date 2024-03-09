from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
class TypeMeal(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class ProductList(models.Model):
    name = models.CharField(max_length=100)
    count = models.DecimalField(max_digits=10, decimal_places=2)
    unit = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

class Recipes(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='recipes')
    title = models.CharField(max_length=100)
    descriptions = models.TextField()
    time_cook = models.TimeField(default='00:30:00')
    products = models.ManyToManyField(ProductList)
    type_meal = models.ForeignKey(TypeMeal, on_delete=models.PROTECT)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    created_add = models.DateField(auto_now_add=True)
    updated_add = models.DateField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'

