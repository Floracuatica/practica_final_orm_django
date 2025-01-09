# Generated by Django 4.1.1 on 2025-01-03 05:27

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laboratorio', '0003_producto_f_fabricacion'),
    ]

    operations = [
        migrations.AddField(
            model_name='directorgeneral',
            name='especialidad',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='laboratorio',
            name='ciudad',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='laboratorio',
            name='pais',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='producto',
            name='f_fabricacion',
            field=models.IntegerField(choices=[(2015, '2015'), (2016, '2016'), (2017, '2017'), (2018, '2018'), (2019, '2019'), (2020, '2020'), (2021, '2021'), (2022, '2022'), (2023, '2023'), (2024, '2024'), (2025, '2025')], validators=[django.core.validators.MinValueValidator(2015), django.core.validators.MaxValueValidator(2025)]),
        ),
    ]
