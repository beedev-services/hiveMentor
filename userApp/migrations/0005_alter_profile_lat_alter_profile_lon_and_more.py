# Generated by Django 4.2.3 on 2023-07-31 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userApp', '0004_profile_weather'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='lat',
            field=models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='lon',
            field=models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='zipCode',
            field=models.CharField(default=0, max_length=10),
        ),
    ]
