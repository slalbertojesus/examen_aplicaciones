# Generated by Django 3.0 on 2019-12-05 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='date_joined',
        ),
        migrations.AlterField(
            model_name='account',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='last login'),
        ),
    ]