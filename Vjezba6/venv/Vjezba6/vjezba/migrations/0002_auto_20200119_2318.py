# Generated by Django 2.2.8 on 2020-01-19 22:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('vjezba', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='projection',
            old_name='projection_name',
            new_name='name',
        ),
        migrations.AddField(
            model_name='projection',
            name='place',
            field=models.CharField(default='Room 1', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='projection',
            name='time',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='users',
            name='is_staff',
            field=models.CharField(default='false', max_length=5),
            preserve_default=False,
        ),
    ]
