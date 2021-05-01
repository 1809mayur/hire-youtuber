# Generated by Django 3.2 on 2021-04-22 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Links',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('fb_link', models.URLField(max_length=300)),
                ('twitter', models.URLField(max_length=300)),
                ('insta_link', models.URLField(max_length=300)),
                ('yt_link', models.URLField(max_length=300)),
                ('mobile', models.CharField(max_length=10)),
                ('country_code', models.CharField(max_length=50)),
            ],
        ),
    ]
