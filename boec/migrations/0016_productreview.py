# Generated by Django 3.2.4 on 2021-06-18 17:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('boec', '0015_empaccount_empaddress_empfullname_employee_processedorder'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(null=True)),
                ('comment', models.CharField(max_length=512)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='boec.account')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='boec.product')),
            ],
        ),
    ]
