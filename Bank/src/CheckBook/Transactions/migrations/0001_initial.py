# Generated by Django 3.1.7 on 2021-03-12 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_Name', models.CharField(blank=True, max_length=50)),
                ('Last_Name', models.CharField(blank=True, max_length=50)),
                ('Starting_Balance', models.DecimalField(blank=True, decimal_places=2, max_digits=10000)),
            ],
        ),
    ]
