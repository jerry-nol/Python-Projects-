# Generated by Django 3.1.7 on 2021-03-16 00:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Transactions', '0014_auto_20210312_2029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='Type',
            field=models.CharField(choices=[('Deposit', 'Deposit'), ('Withdrawal', 'Withdrawal')], max_length=60),
        ),
    ]
