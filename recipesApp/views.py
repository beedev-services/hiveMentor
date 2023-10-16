# views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *

def recipeDash(request):
    return render(request, 'recipeDash.html')

def createRecipe(request):
    if request.method == 'POST':
        theRecipeForm = RecipeForm(request.POST)
        theRecipeImageForm = RecipeImageForm(request.POST, request.FILES)
        ingredientFormset = IngredientFormSet(request.POST, prefix='ingredient')
        instructionFormset = InstructionFormSet(request.POST, prefix='instruction')

        if theRecipeForm.is_valid() and theRecipeImageForm.is_valid() and ingredientFormset.is_valid() and instructionFormset.is_valid():
            recipe = theRecipeForm.save()
            theRecipeImageForm.instance = recipe
            theRecipeImageForm.save()
            ingredientFormset.instance = recipe
            ingredientFormset.save()
            instructionFormset.instance = recipe
            instructionFormset.save()
            return redirect('/recipes/', pk=recipe.pk)
    else:
        theRecipeForm = RecipeForm()
        theRecipeImageForm = RecipeImageForm()
        ingredientFormset = IngredientFormSet(prefix='ingredient')
        instructionFormset = InstructionFormSet(prefix='instruction')

    return render(request, 'createRecipe.html', {
        'theRecipeForm': theRecipeForm,
        'theRecipeImageForm': theRecipeImageForm,
        'ingredientFormset': ingredientFormset,
        'instructionFormset': instructionFormset,
    })

def updateRecipe(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)

    if request.method == 'POST':
        theRecipeForm = RecipeForm(request.POST, instance=recipe)
        theRecipeImageForm = RecipeImageForm(request.POST, request.FILES, instance=recipe.recipeimage)

        if theRecipeForm.is_valid() and theRecipeImageForm.is_valid():
            recipe = theRecipeForm.save()
            theRecipeImageForm.save()
            return redirect('/recipes/dashboard/', pk=recipe.pk)
    else:
        theRecipeForm = RecipeForm(instance=recipe)
        theRecipeImageForm = RecipeImageForm(instance=recipe.recipeimage)

    return render(request, 'updateRecipe.html', {
        'theRecipeForm': theRecipeForm,
        'theRecipeImageForm': theRecipeImageForm,
    })

def recipe_detail(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    ingredients = recipe.ingredient_set.all()
    instructions = recipe.instruction_set.all()
    return render(request, 'recipeDetail.html', {
        'recipe': recipe,
        'ingredients': ingredients,
        'instructions': instructions,
    })
