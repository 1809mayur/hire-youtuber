# Generated by Django 3.2 on 2021-04-22 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('links', '0002_auto_20210422_2004'),
    ]

    operations = [
        migrations.AddField(
            model_name='links',
            name='country_code',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='links',
            name='mobile',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]
