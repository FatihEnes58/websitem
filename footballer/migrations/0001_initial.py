# Generated by Django 3.1.7 on 2021-02-27 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Footballer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Oyuncu Adı')),
                ('age', models.IntegerField(verbose_name='Oyuncu Yaşı')),
                ('position', models.CharField(choices=[('fv', 'Forvet'), ('os', 'Ortasaha'), ('def', 'Defans'), ('kl', 'Kaleci')], default='fv', max_length=10)),
                ('salary', models.IntegerField(verbose_name='Oyuncunun Maaşı')),
                ('marketValue', models.IntegerField(verbose_name='Oyuncunun değeri')),
            ],
        ),
    ]