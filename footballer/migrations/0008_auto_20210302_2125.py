# Generated by Django 3.1.7 on 2021-03-02 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('footballteam', '0002_auto_20210301_1342'),
        ('footballer', '0007_auto_20210302_1240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='footballer',
            name='team',
            field=models.ManyToManyField(blank=True, to='footballteam.FootballTeam', verbose_name='Takım'),
        ),
    ]
