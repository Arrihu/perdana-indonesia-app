# Generated by Django 2.2 on 2020-12-30 02:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0003_club_organisation_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='club',
            name='date_register',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='club',
            name='organisation_id',
            field=models.CharField(blank=True, max_length=100, null=True, unique=True),
        ),
    ]
