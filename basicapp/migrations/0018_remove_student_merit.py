# Generated by Django 3.0.3 on 2020-08-02 20:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basicapp', '0017_student_merit'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='merit',
        ),
    ]
