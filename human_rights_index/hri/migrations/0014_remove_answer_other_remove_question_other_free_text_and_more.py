# Generated by Django 5.1.1 on 2024-11-03 12:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hri', '0013_alter_text_notes_alter_text_notes_en_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='other',
        ),
        migrations.RemoveField(
            model_name='question',
            name='other_free_text',
        ),
        migrations.AlterField(
            model_name='answer',
            name='option',
            field=models.CharField(blank=True, choices=[('0', 'Zero point answer'), ('1', 'One point answer'), ('2', 'Two points answer')], max_length=255, null=True, verbose_name='option'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hri.question', verbose_name='question'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='survey',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hri.survey', verbose_name='survey'),
        ),
        migrations.AlterField(
            model_name='group',
            name='code',
            field=models.CharField(max_length=255, unique=True, verbose_name='code'),
        ),
        migrations.AlterField(
            model_name='group',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='group',
            name='score',
            field=models.FloatField(blank=True, null=True, verbose_name='score'),
        ),
        migrations.AlterField(
            model_name='question',
            name='answer_0_points',
            field=models.TextField(blank=True, null=True, verbose_name='answer for 0 points'),
        ),
        migrations.AlterField(
            model_name='question',
            name='answer_0_points_en',
            field=models.TextField(blank=True, null=True, verbose_name='answer for 0 points'),
        ),
        migrations.AlterField(
            model_name='question',
            name='answer_0_points_lt',
            field=models.TextField(blank=True, null=True, verbose_name='answer for 0 points'),
        ),
        migrations.AlterField(
            model_name='question',
            name='answer_0_points_pt',
            field=models.TextField(blank=True, null=True, verbose_name='answer for 0 points'),
        ),
        migrations.AlterField(
            model_name='question',
            name='answer_0_points_sk',
            field=models.TextField(blank=True, null=True, verbose_name='answer for 0 points'),
        ),
        migrations.AlterField(
            model_name='question',
            name='answer_1_points',
            field=models.TextField(blank=True, null=True, verbose_name='answer for one point'),
        ),
        migrations.AlterField(
            model_name='question',
            name='answer_1_points_en',
            field=models.TextField(blank=True, null=True, verbose_name='answer for one point'),
        ),
        migrations.AlterField(
            model_name='question',
            name='answer_1_points_lt',
            field=models.TextField(blank=True, null=True, verbose_name='answer for one point'),
        ),
        migrations.AlterField(
            model_name='question',
            name='answer_1_points_pt',
            field=models.TextField(blank=True, null=True, verbose_name='answer for one point'),
        ),
        migrations.AlterField(
            model_name='question',
            name='answer_1_points_sk',
            field=models.TextField(blank=True, null=True, verbose_name='answer for one point'),
        ),
        migrations.AlterField(
            model_name='question',
            name='answer_2_points',
            field=models.TextField(blank=True, null=True, verbose_name='answer for 2 points'),
        ),
        migrations.AlterField(
            model_name='question',
            name='answer_2_points_en',
            field=models.TextField(blank=True, null=True, verbose_name='answer for 2 points'),
        ),
        migrations.AlterField(
            model_name='question',
            name='answer_2_points_lt',
            field=models.TextField(blank=True, null=True, verbose_name='answer for 2 points'),
        ),
        migrations.AlterField(
            model_name='question',
            name='answer_2_points_pt',
            field=models.TextField(blank=True, null=True, verbose_name='answer for 2 points'),
        ),
        migrations.AlterField(
            model_name='question',
            name='answer_2_points_sk',
            field=models.TextField(blank=True, null=True, verbose_name='answer for 2 points'),
        ),
        migrations.AlterField(
            model_name='question',
            name='question',
            field=models.TextField(verbose_name='question'),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_en',
            field=models.TextField(null=True, verbose_name='question'),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_lt',
            field=models.TextField(null=True, verbose_name='question'),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_pt',
            field=models.TextField(null=True, verbose_name='question'),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_sk',
            field=models.TextField(null=True, verbose_name='question'),
        ),
        migrations.AlterField(
            model_name='question',
            name='weight_choice',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='hri.weight', verbose_name='weight choice'),
        ),
        migrations.AlterField(
            model_name='survey',
            name='group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='hri.group', verbose_name='group'),
        ),
        migrations.AlterField(
            model_name='survey',
            name='score',
            field=models.FloatField(blank=True, null=True, verbose_name='score'),
        ),
        migrations.AlterField(
            model_name='survey',
            name='weight',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='hri.weight', verbose_name='weight'),
        ),
        migrations.AlterField(
            model_name='text',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='created at'),
        ),
        migrations.AlterField(
            model_name='text',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='updated at'),
        ),
        migrations.AlterField(
            model_name='weight',
            name='weight_question',
            field=models.TextField(blank=True, null=True, verbose_name='weight_answer'),
        ),
        migrations.AlterField(
            model_name='weight',
            name='weight_question_en',
            field=models.TextField(blank=True, null=True, verbose_name='weight_answer'),
        ),
        migrations.AlterField(
            model_name='weight',
            name='weight_question_lt',
            field=models.TextField(blank=True, null=True, verbose_name='weight_answer'),
        ),
        migrations.AlterField(
            model_name='weight',
            name='weight_question_pt',
            field=models.TextField(blank=True, null=True, verbose_name='weight_answer'),
        ),
        migrations.AlterField(
            model_name='weight',
            name='weight_question_sk',
            field=models.TextField(blank=True, null=True, verbose_name='weight_answer'),
        ),
    ]
