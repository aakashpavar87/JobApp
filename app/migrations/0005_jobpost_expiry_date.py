# Generated by Django 5.0.4 on 2024-05-07 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_jobpost_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobpost',
            name='expiry_date',
            field=models.DateField(null=True),
        ),
    ]