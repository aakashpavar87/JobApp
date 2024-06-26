# Generated by Django 5.0.6 on 2024-05-11 11:54

import django.core.validators
import subscribe.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscribe', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscribe',
            name='email',
            field=models.CharField(max_length=100, validators=[django.core.validators.EmailValidator(message='Enter valid Email')]),
        ),
        migrations.AlterField(
            model_name='subscribe',
            name='first_name',
            field=models.CharField(max_length=100, validators=[subscribe.models.validate_char, subscribe.models.validate_comma]),
        ),
        migrations.AlterField(
            model_name='subscribe',
            name='last_name',
            field=models.CharField(max_length=100, validators=[subscribe.models.validate_char, subscribe.models.validate_comma]),
        ),
    ]
