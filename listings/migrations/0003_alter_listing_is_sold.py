# Generated by Django 3.2.2 on 2021-05-10 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0002_listing_is_sold'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='is_sold',
            field=models.BooleanField(default=True),
        ),
    ]
