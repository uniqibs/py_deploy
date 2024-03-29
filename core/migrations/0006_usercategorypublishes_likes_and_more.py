# Generated by Django 5.0 on 2024-01-04 11:04

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_usercategoricpublish_config'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserCategoryPublishes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sell', models.CharField(max_length=50, verbose_name='цена')),
                ('name', models.CharField(max_length=50, verbose_name='название продукта')),
                ('category_product', models.CharField(choices=[('ТЕХНИКА', 'ТЕХНИКА'), ('ОДЕЖДА', 'ОДЕЖДА'), ('ДОМ', 'ДОМ'), ('БИСНЕС', 'БИЗНЕС'), ('ЕДА', 'ЕДА'), ('ДРУГОЕ', 'ДРУГОЕ')], max_length=50, verbose_name='категория продуктов')),
                ('country', models.CharField(choices=[('Абхазия', 'Абхазия'), ('Австралия', 'Австралия'), ('Австрия', 'Австрия'), ('Азербайджан', 'Азербайджан'), ('Албания', 'Албания'), ('Алжир', 'Алжир'), ('Андорра', 'Андорра'), ('Аргентина', 'Аргентина'), ('Армения', 'Армения'), ('Аруба', 'Аруба'), ('Афганистан', 'Афганистан'), ('Багамы', 'Багамы'), ('Бангладеш', 'Бангладеш'), ('Барбадос', 'Барбадос'), ('Великобритания', 'Великобритания'), ('Германия', 'Германия'), ('Грузия', 'Грузия'), ('Катар', 'Катар'), ('Канада', 'Канада'), ('Россия', 'Россия'), ('Россия', 'Россия'), ('США', 'США'), ('Узбекситан', 'Узбекситан'), ('Украина', 'Украина'), ('Швейцария', 'Швейцария'), ('Швеция', 'Швеция')], max_length=50, verbose_name='название страны')),
                ('telphone_number', models.CharField(max_length=50, verbose_name='телефон номер')),
                ('good_or_bad_or_norm', models.CharField(choices=[('В ОТЛИЧНОМ СОСТОЯНИЕ', 'В ОТЛИЧНОМ СОСТОЯНИЕ'), ('В ПЛОХОМ СОСТОЯНИЕ', 'В ПЛОХОМ СОСТОЯНИЕ'), ('В НОРМАЛЬНОМ СОСТОЯНИЕ', 'В НОРМАЛЬНОМ СОСТОЯНИЕ'), ('В Б/У СОСТОЯНИЕ', 'В Б/У СОСТОЯНИЕ')], max_length=50, verbose_name='качество товара')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Likes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('like', models.BooleanField(blank=True, max_length=50)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('publish_objects', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.usercategorypublishes')),
            ],
        ),
        migrations.DeleteModel(
            name='UserCategoricPublish',
        ),
    ]
