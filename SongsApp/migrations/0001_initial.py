# Generated by Django 3.2.6 on 2021-08-10 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('song_title', models.CharField(max_length=200)),
                ('singer', models.CharField(max_length=200)),
                ('release_date', models.DateField(verbose_name='release date')),
            ],
        ),
    ]
