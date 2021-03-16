# Generated by Django 3.1.7 on 2021-03-12 23:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Transactions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date_of_Transaction', models.DateField()),
                ('Type', models.CharField(choices=[('Withdrawal', 'Withdrawal'), ('Deposit', 'Deposit')], max_length=60)),
                ('Amount', models.DecimalField(blank=True, decimal_places=2, max_digits=1000)),
                ('Description', models.TextField(default='', max_length=200)),
                ('Account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Transactions.account')),
            ],
        ),
    ]
