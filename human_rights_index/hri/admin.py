from django.contrib import admin

# Register your models here.
from django.contrib import admin
from hri.models import Group, Question, Survey, Answer, Weight, Text


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'code')
    search_fields = ('name', 'code')


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question', 'answer_0_points', 'answer_1_points', 'answer_2_points', 'weight_choice')
    search_fields = ('question', )


@admin.register(Survey)
class SurveyAdmin(admin.ModelAdmin):
    list_display = ('id', 'group')
    search_fields = ('group__code', )
    list_filter = ('group',)


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('question', 'survey__id', 'option')
    search_fields = ('question__question', 'survey__id')
    list_filter = ('survey__id', 'question', 'option', 'survey__group__code')


@admin.register(Weight)
class WeightAdmin(admin.ModelAdmin):
    list_display = ('weight_question', )


@admin.register(Text)
class TextAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
