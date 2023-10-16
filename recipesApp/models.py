from django.db import models
from django.db.models.deletion import CASCADE
from userApp.models import *

class Recipe(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    recipeOwner =  models.ForeignKey(User, related_name="theRecipeOwner", on_delete=CASCADE)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title
    
class RecipeImage(models.Model):
    recipe = models.OneToOneField(Recipe, unique=True, on_delete=CASCADE)
    image = models.ImageField(upload_to="recipes")
    def __str__(self):
        return f'{self.recipe.title} RecipeImage'
    
def create_recipe_image(sender, instance, created, **kwargs):
    if created:
        Recipe.objects.create(recipe=instance)
        post_save.connect(create_recipe_image, sender=Recipe)

class Ingredient(models.Model):
    aRecipe = models.ForeignKey(Recipe, related_name="theRecipe",on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    quantity = models.CharField(max_length=20)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

class Instruction(models.Model):
    forRecipe = models.ForeignKey(Recipe, related_name="theNewRecipe", on_delete=models.CASCADE)
    step_number = models.PositiveIntegerField()
    description = models.TextField()
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)