# Generated by Django 5.0 on 2024-01-10 14:31

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_usercategorypublishes_one_photo'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='usercategorypublishes',
            name='second_photo',
            field=models.ImageField(null=True, upload_to='img/', verbose_name='2 фото'),
        ),
        migrations.AddField(
            model_name='usercategorypublishes',
            name='street',
            field=models.CharField(default=1, max_length=50, verbose_name='улица'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='usercategorypublishes',
            name='one_photo',
            field=models.ImageField(null=True, upload_to='img/', verbose_name='1 фото'),
        ),
        migrations.CreateModel(
            name='UserPhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_photo', models.ImageField(null=True, upload_to='user_photo/')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]