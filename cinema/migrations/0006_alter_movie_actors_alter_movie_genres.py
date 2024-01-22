# Generated by Django 4.1 on 2024-01-14 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0005_rename_seats_in_rows_cinemahall_seats_in_row'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='actors',
            field=models.ManyToManyField(default=None, to='cinema.actor'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='genres',
            field=models.ManyToManyField(default=None, to='cinema.genre'),
        ),
    ]