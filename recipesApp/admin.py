from django.contrib import admin
from .models import *

admin.site.register(Recipe)
admin.site.register(RecipeImage)
admin.site.register(Ingredient)
admin.site.register(Instruction)
