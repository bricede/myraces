# Generated by Django 3.0.5 on 2020-05-04 12:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('races', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='race',
            name='date_added',
        ),
        migrations.AlterField(
            model_name='race',
            name='date',
            field=models.DateField(default=datetime.date(2020, 5, 4)),
        ),
    ]
