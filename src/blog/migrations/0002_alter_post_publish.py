# Generated by Django 4.2.4 on 2023-08-14 11:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='publish',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 14, 11, 41, 49, 70535, tzinfo=datetime.timezone.utc)),
        ),
    ]
