# Generated by Django 3.2.18 on 2023-06-27 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend_app', '0002_alter_favorite_unique_together'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='favorite',
            constraint=models.UniqueConstraint(fields=('user_id', 'music_id'), name='unique'),
        ),
    ]