<<<<<<< HEAD
# Generated by Django 4.2.3 on 2023-08-20 02:03
=======
# Generated by Django 4.2.3 on 2023-08-17 22:07
>>>>>>> fddc3ddcc9e0a2089a6976086ca8e4a13530f56b

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logApp', '0013_food_foodcat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='foodCat',
            field=models.CharField(default='Meats', max_length=255),
        ),
    ]
