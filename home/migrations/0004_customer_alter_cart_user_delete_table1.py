# Generated by Django 5.0.4 on 2024-05-25 06:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_orderdetails_ordertable_cart_cartitem'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', max_length=50, null=True)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('gender', models.CharField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', max_length=10, null=True)),
                ('address', models.CharField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', max_length=255, null=True)),
                ('password', models.CharField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', max_length=255, null=True)),
            ],
            options={
                'db_table': 'Customer',
                'managed': False,
            },
        ),
        migrations.AlterField(
            model_name='cart',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.customer'),
        ),
        migrations.DeleteModel(
            name='Table1',
        ),
    ]
