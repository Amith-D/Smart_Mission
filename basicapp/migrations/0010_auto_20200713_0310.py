# Generated by Django 3.0.3 on 2020-07-12 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basicapp', '0009_auto_20200713_0308'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='III_sem',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='II_sem',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='IV_sem',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='I_sem',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='VIII_sem',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='VII_sem',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='VI_sem',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='V_sem',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='pred_avg_marks',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='pred_cocur',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='pred_intern',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='pred_pack',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
