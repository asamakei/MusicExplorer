# Generated by Django 3.2.18 on 2023-06-20 13:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('genre_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Music',
            fields=[
                ('music_id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('url', models.URLField()),
                ('position_x', models.FloatField()),
                ('position_y', models.FloatField()),
                ('views', models.IntegerField()),
                ('good', models.IntegerField()),
                ('bad', models.IntegerField()),
                ('comment_count', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='AppUser',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, unique=True)),
                ('password', models.CharField(max_length=255)),
                ('twitter_id', models.CharField(max_length=255)),
                ('instagram_id', models.CharField(max_length=255)),
                ('age', models.IntegerField()),
                ('gender', models.IntegerField()),
                ('genre_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend_app.genre')),
            ],
        ),
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('music_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend_app.music')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend_app.appuser')),
            ],
            options={
                'unique_together': {('user_id', 'music_id')},
            },
        ),
    ]
