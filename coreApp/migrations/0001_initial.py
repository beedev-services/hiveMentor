# Generated by Django 4.2.3 on 2023-08-07 22:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Version',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('versionNum', models.CharField(max_length=255)),
                ('versionRelease', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('info', models.TextField()),
                ('version', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='theVersion', to='coreApp.version')),
            ],
        ),
    ]
