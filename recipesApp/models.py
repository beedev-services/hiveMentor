from django.db import models
from django.db.models.deletion import CASCADE
from userApp.models import User

meals = [
    ('Breakfast', 'Breakfast'),
    ('Lunch', 'Lunch'),
    ('Dinner','Dinner'),
    ('Snack','Snack'),
]
categories = [
    {'id': 1, 'name': 'Grains'},
    {'id': 2, 'name': 'Dairy'},
    {'id': 3, 'name': 'Fruits'},
    {'id': 4, 'name': 'Meats'},
    {'id': 5, 'name': 'Fish & Seafood'},
    {'id': 6, 'name': 'Vegetables'},
    {'id': 7, 'name': 'Other Proteins'},
    {'id': 8, 'name': 'Nuts & Seeds'},
    {'id': 9, 'name': 'Beverages'},
    {'id': 10, 'name': 'Other Starches'},
]


class Recipe(models.Model):
    title = models.CharField(max_length=255)
    ingredients = models.TextField()
    instructions = models.TextField()
    meal = models.CharField(max_length=255, choices=meals, blank=True)
    servings = models.IntegerField(default=1)
    comments = models.TextField(blank=True)
    totalCals = models.IntegerField(default=0)
    foodCat = models.CharField(max_length=255, choices=categories, default='Meats')
    cooker = models.ForeignKey(User, related_name='theCooker', on_delete=CASCADE)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

class SaveRecipe(models.Model):
    recipe = models.ForeignKey(Recipe, related_name='theRecipe', on_delete=CASCADE)
    baker = models.ForeignKey(User, related_name='theBaker', on_delete=CASCADE)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
