# Generated by Django 2.2.17 on 2021-01-17 03:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('easy_logging', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='easylogging',
            old_name='ip_addres',
            new_name='ip_address',
        ),
    ]
