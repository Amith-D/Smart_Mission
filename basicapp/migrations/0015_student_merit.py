# Generated by Django 3.0.3 on 2020-08-02 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basicapp', '0014_auto_20200714_0409'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='merit',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
