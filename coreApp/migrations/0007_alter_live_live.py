# Generated by Django 4.2.3 on 2023-08-21 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coreApp', '0006_alter_release_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='live',
            name='live',
            field=models.CharField(default='backlog', max_length=255),
        ),
    ]
