# Generated by Django 4.1.2 on 2023-01-06 01:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('family', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PetRace', models.CharField(max_length=100)),
                ('Age', models.FloatField()),
                ('Name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Vehicles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Brand', models.CharField(max_length=100)),
                ('Model', models.CharField(max_length=100)),
                ('Colour', models.CharField(max_length=100)),
            ],
        ),
    ]
