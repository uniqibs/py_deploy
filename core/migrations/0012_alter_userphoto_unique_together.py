# Generated by Django 5.0 on 2024-01-10 14:56

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_usercategorypublishes_second_photo_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='userphoto',
            unique_together={('user',)},
        ),
    ]