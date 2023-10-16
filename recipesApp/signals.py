from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import *


@receiver(post_save, sender=Recipe)
def createRecipeImage(sender, instance, created, **kwargs):
    if created:
        RecipeImage.objects.create(recipeImage=instance)

@receiver(post_save, sender=Recipe)
def saveRecipeImage(sender, instance, **kwargs):
    instance.recipeImage.save()