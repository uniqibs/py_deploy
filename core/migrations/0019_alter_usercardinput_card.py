# Generated by Django 5.0 on 2024-01-12 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0018_usercardinput_type_card'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usercardinput',
            name='card',
            field=models.IntegerField(max_length=19, verbose_name='номер карты'),
        ),
    ]