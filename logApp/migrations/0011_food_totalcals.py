# Generated by Django 4.2.3 on 2023-08-17 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logApp', '0010_remove_food_food_food_fooditem'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='totalCals',
            field=models.IntegerField(default=0),
        ),
    ]
