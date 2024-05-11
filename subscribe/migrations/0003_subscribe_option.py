# Generated by Django 5.0.6 on 2024-05-11 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscribe', '0002_alter_subscribe_email_alter_subscribe_first_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscribe',
            name='option',
            field=models.CharField(choices=[('W', 'Weekly'), ('M', 'Monthly')], default='W', max_length=2),
        ),
    ]
