# Generated by Django 3.2.4 on 2021-06-15 06:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('boec', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('discount', models.IntegerField(null=True)),
                ('title', models.CharField(max_length=256, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('priceEntry', models.IntegerField()),
                ('dateEntry', models.DateField(null=True)),
                ('publicationDate', models.DateField(null=True)),
                ('barcode', models.CharField(max_length=256, null=True)),
                ('producer', models.CharField(max_length=256, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('product_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='boec.product')),
                ('author', models.CharField(max_length=256, null=True)),
                ('status', models.CharField(max_length=256)),
                ('type', models.CharField(max_length=256)),
            ],
            bases=('boec.product',),
        ),
        migrations.CreateModel(
            name='Clothes',
            fields=[
                ('product_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='boec.product')),
                ('band', models.CharField(max_length=256, null=True)),
                ('size', models.CharField(max_length=256)),
            ],
            bases=('boec.product',),
        ),
        migrations.CreateModel(
            name='Electronic',
            fields=[
                ('product_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='boec.product')),
                ('specification', models.CharField(max_length=256)),
                ('warrantyPeriodDate', models.IntegerField(null=True)),
                ('origin', models.CharField(max_length=256, null=True)),
            ],
            bases=('boec.product',),
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(null=True)),
                ('total', models.IntegerField(null=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='boec.account')),
            ],
        ),
    ]
