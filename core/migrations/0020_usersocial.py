# Generated by Django 5.0 on 2024-01-13 10:11

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_alter_usercardinput_card'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserSocial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='username')),
                ('type_social_media', models.CharField(choices=[('TELEGRAM', 'TELEGRAM'), ('INSTAGRAM', 'INSTAGRAM'), ('FACEBOOK', 'FACCEBOOK')], max_length=50, verbose_name='какую социальную сеть вы исьпользуету')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
