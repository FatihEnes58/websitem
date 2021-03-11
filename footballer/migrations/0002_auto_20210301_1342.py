# Generated by Django 3.1.7 on 2021-03-01 10:42

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('footballer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='footballer',
            name='overall',
            field=models.IntegerField(default=70, validators=[django.core.validators.MinValueValidator(40), django.core.validators.MaxValueValidator(99)], verbose_name='Oyuncunun Gücü(40-99)'),
        ),
        migrations.AlterField(
            model_name='footballer',
            name='age',
            field=models.IntegerField(default=17, validators=[django.core.validators.MinValueValidator(15), django.core.validators.MaxValueValidator(50)], verbose_name='Oyuncu Yaşı'),
        ),
    ]
