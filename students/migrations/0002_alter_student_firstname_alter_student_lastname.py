# Generated by Django 4.1.2 on 2022-10-31 05:15

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='firstname',
            field=models.CharField(max_length=32, validators=[django.core.validators.RegexValidator(message='name must be at least 3 letters and contain only lowercase letters except the first one must be uppercase', regex='^[A-Z][a-z]+$')]),
        ),
        migrations.AlterField(
            model_name='student',
            name='lastname',
            field=models.CharField(max_length=32, validators=[django.core.validators.RegexValidator(message='name must be at least 3 letters and contain only lowercase letters except the first one must be uppercase', regex='^[A-Z][a-z]+$')]),
        ),
    ]
