# Generated by Django 3.2.4 on 2021-06-16 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boec', '0004_remove_item_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='price',
            field=models.IntegerField(null=True),
        ),
    ]
