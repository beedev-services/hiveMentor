# Generated by Django 4.2.4 on 2023-08-28 02:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coreApp', '0007_alter_live_live'),
    ]

    operations = [
        migrations.AlterField(
            model_name='live',
            name='live',
            field=models.CharField(default='BackLog', max_length=255),
        ),
    ]
