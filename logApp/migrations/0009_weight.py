# Generated by Django 4.2.3 on 2023-08-17 03:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userApp', '0006_profile_weight'),
        ('logApp', '0008_foodlist_remove_food_calories_food_servings_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Weight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.IntegerField()),
                ('unit', models.CharField(default='LBS', max_length=255)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
                ('day', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='theDay', to='logApp.day')),
                ('userWeight', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='theUserWeight', to='userApp.user')),
            ],
        ),
    ]