# Generated by Django 4.2.3 on 2023-10-16 20:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('userApp', '0006_profile_weight'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
                ('recipeOwner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='theRecipeOwner', to='userApp.user')),
            ],
        ),
        migrations.CreateModel(
            name='RecipeImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='recipes')),
                ('recipe', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='recipesApp.recipe')),
            ],
        ),
        migrations.CreateModel(
            name='Instruction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('step_number', models.PositiveIntegerField()),
                ('description', models.TextField()),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
                ('forRecipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='theNewRecipe', to='recipesApp.recipe')),
            ],
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('quantity', models.CharField(max_length=20)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
                ('aRecipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='theRecipe', to='recipesApp.recipe')),
            ],
        ),
    ]
