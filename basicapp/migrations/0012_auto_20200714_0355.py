# Generated by Django 3.0.3 on 2020-07-13 22:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basicapp', '0011_student_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='Time',
            field=models.DateTimeField(default=datetime.date.today, editable=False),
        ),
    ]