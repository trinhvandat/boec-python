# Generated by Django 3.2.4 on 2021-06-18 13:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('boec', '0014_order_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmpAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=256)),
                ('password', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='EmpAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numberHouse', models.CharField(max_length=256)),
                ('street', models.CharField(max_length=256)),
                ('district', models.CharField(max_length=256)),
                ('city', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='EmpFullName',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=256)),
                ('midName', models.CharField(max_length=256)),
                ('lastName', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=256)),
                ('code', models.CharField(max_length=256)),
                ('salary', models.FloatField(max_length=256)),
                ('position', models.CharField(max_length=256)),
                ('dob', models.DateField(null=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='boec.empaccount')),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='boec.empaddress')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='boec.empfullname')),
            ],
        ),
        migrations.CreateModel(
            name='ProcessedOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('processDate', models.DateField(null=True)),
                ('status', models.CharField(max_length=256)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='boec.employee')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='boec.order')),
            ],
        ),
    ]
