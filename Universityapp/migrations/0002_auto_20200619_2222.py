# Generated by Django 3.0.3 on 2020-06-19 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Universityapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student_data',
            name='Distance',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='student_data',
            name='Tenth_Board',
            field=models.FloatField(choices=[('1', 'STATE'), ('2', 'CBSE'), ('3', 'ICSE')], null=True),
        ),
        migrations.AlterField(
            model_name='student_data',
            name='Tenth_Eng',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='student_data',
            name='Tenth_Math',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='student_data',
            name='Tenth_Medium',
            field=models.FloatField(choices=[('1', 'English'), ('2', 'Kannada')], null=True),
        ),
        migrations.AlterField(
            model_name='student_data',
            name='Tenth_Science',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='student_data',
            name='Tenth_Total',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='student_data',
            name='Twelth_Board',
            field=models.FloatField(choices=[('1', 'STATE'), ('2', 'CBSE'), ('3', 'ICSE')], null=True),
        ),
        migrations.AlterField(
            model_name='student_data',
            name='Twelth_Chemistry',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='student_data',
            name='Twelth_Eng',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='student_data',
            name='Twelth_Math',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='student_data',
            name='Twelth_Optional',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='student_data',
            name='Twelth_Physics',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='student_data',
            name='Twelth_Total',
            field=models.FloatField(null=True),
        ),
    ]
