# Generated by Django 5.1.1 on 2024-10-20 13:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hri', '0003_remove_survey_survey_alter_survey_group'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='weight',
            name='weight_option',
        ),
        migrations.AddField(
            model_name='survey',
            name='weight',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='hri.weight'),
        ),
    ]
