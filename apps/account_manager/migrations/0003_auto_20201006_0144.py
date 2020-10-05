# Generated by Django 3.1.2 on 2020-10-06 01:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account_manager', '0002_account'),
    ]

    operations = [
        migrations.AddField(
            model_name='baseuser',
            name='first_name',
            field=models.CharField(max_length=255, null=True, verbose_name='First Name'),
        ),
        migrations.AddField(
            model_name='baseuser',
            name='last_name',
            field=models.CharField(max_length=255, null=True, verbose_name='Last Name'),
        ),
    ]