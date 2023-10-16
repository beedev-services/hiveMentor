# forms.py
from django import forms
from django.forms import inlineformset_factory
from .models import *

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'description', 'recipeOwner']  # Add other fields as needed

RecipeImageForm = inlineformset_factory(Recipe, RecipeImage, fields=('image',), can_delete=False, extra=1)
IngredientFormSet = inlineformset_factory(Recipe, Ingredient, fields=('name', 'quantity'), can_delete=False, extra=1)
InstructionFormSet = inlineformset_factory(Recipe, Instruction, fields=('step_number', 'description'), can_delete=False, extra=1)
