# Generated by Django 3.1.7 on 2021-03-12 23:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Transactions', '0004_auto_20210312_1647'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='Type',
            field=models.CharField(choices=[('Deposit', 'Deposit'), ('Withdrawal', 'Withdrawal')], max_length=60),
        ),
    ]