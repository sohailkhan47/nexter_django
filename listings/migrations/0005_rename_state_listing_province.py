# Generated by Django 3.2.2 on 2021-05-11 18:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0004_alter_listing_is_sold'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listing',
            old_name='state',
            new_name='province',
        ),
    ]
