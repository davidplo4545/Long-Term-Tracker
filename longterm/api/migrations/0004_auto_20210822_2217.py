# Generated by Django 3.2.4 on 2021-08-22 19:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_israelpaper_currency'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='crypto',
            name='five_year_return',
        ),
        migrations.RemoveField(
            model_name='israelpaper',
            name='five_year_return',
        ),
        migrations.RemoveField(
            model_name='uspaper',
            name='five_year_return',
        ),
    ]
