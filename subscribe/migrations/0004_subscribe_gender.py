# Generated by Django 5.0.6 on 2024-05-11 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscribe', '0003_subscribe_option'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscribe',
            name='gender',
            field=models.CharField(default='M', max_length=2),
        ),
    ]
