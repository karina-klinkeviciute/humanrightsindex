# Generated by Django 5.1.1 on 2024-10-20 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hri', '0009_remove_question_score'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='code',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
