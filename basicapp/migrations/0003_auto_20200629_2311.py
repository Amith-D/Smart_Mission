# Generated by Django 3.0.3 on 2020-06-29 17:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basicapp', '0002_auto_20200621_1317'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='FatherQualification',
            new_name='Father_Qualification',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='Levelof_achievement',
            new_name='Level_of_achievement',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='MotherQualification',
            new_name='Mother_Qualification',
        ),
    ]
