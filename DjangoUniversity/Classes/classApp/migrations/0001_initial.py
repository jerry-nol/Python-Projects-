# Generated by Django 3.1.7 on 2021-03-04 23:34

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='djangoClasses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('course_number', models.IntegerField(blank=True, default='', validators=[django.core.validators.MaxValueValidator(3)])),
                ('instructor', models.CharField(blank=True, default='', max_length=60)),
                ('duration', models.DecimalField(blank=True, decimal_places=2, default='', max_digits=3)),
            ],
        ),
    ]
