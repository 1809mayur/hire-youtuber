# Generated by Django 3.2 on 2021-04-22 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hireyoutuber', '0002_alter_hiretuber_mobile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hiretuber',
            name='email',
            field=models.EmailField(blank=True, max_length=254),
        ),
    ]
