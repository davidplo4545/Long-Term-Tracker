# Generated by Django 3.2.4 on 2021-08-22 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20210822_1442'),
    ]

    operations = [
        migrations.AlterField(
            model_name='israelpaper',
            name='currency',
            field=models.CharField(default='ILS', editable=False, max_length=9),
        ),
    ]
