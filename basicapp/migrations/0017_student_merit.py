# Generated by Django 3.0.3 on 2020-08-02 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basicapp', '0016_remove_student_merit'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='merit',
            field=models.FloatField(blank=True, null=True),
        ),
    ]