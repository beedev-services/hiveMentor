# Generated by Django 4.2.3 on 2023-09-15 02:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('logApp', '0017_remove_work_unit'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fitness',
            name='unit',
        ),
    ]