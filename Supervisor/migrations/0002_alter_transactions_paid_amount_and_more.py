# Generated by Django 4.1.5 on 2023-01-19 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Supervisor', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transactions',
            name='paid_amount',
            field=models.IntegerField(blank=True, db_column='Paid_amount', null=True),
        ),
        migrations.AlterField(
            model_name='transactions',
            name='total_profit',
            field=models.IntegerField(blank=True, db_column='Total_Profit', null=True),
        ),
    ]