# Generated by Django 3.0.3 on 2020-07-12 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basicapp', '0004_auto_20200712_0409'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='pred_avg_marks',
            field=models.FloatField(null=True),
        ),
    ]
