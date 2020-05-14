# Generated by Django 2.2.10 on 2020-03-26 16:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('club', '0001_initial'),
        ('member', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bow',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bows', to='member.BaseMember'),
        ),
        migrations.AddField(
            model_name='arrow',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='arrows', to='member.BaseMember'),
        ),
        migrations.AddField(
            model_name='archeryrange',
            name='managed_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='archery_ranges', to='club.ClubUnit'),
        ),
    ]
