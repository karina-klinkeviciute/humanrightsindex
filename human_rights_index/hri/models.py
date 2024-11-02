from django.db import models
from django.db.models import Avg

from django.utils.translation import gettext_lazy as _


class Group(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    code = models.CharField(max_length=255, unique=True)
    score = models.FloatField(null=True, blank=True)

    def calculate_score(self):
        self.score = self.survey_set.aggregate(Avg('score'))['score__avg']
        self.save()


class Weight(models.Model):
    weight_question = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.weight_question


class Question(models.Model):
    question = models.TextField()
    answer_0_points = models.TextField(null=True, blank=True)
    answer_1_points = models.TextField(null=True, blank=True)
    answer_2_points = models.TextField(null=True, blank=True)
    other_free_text = models.BooleanField(default=False, null=True, blank=True)
    weight_choice = models.ForeignKey(Weight, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.question


class Survey(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE, null=True, blank=True)
    score = models.FloatField(null=True, blank=True)
    weight = models.ForeignKey('Weight', on_delete=models.SET_NULL, null=True, blank=True)

    def calculate_score(self):
        score = 0
        for answer in Answer.objects.filter(survey=self):
            if answer.option == "0":
                answer_score = 0
            if answer.option == "1":
                answer_score = 1
            if answer.option == "2":
                answer_score = 2

            if self.weight and self.weight == answer.question.weight_choice:
                answer_score -= 1

            score += answer_score

        maximal_possible_score = Question.objects.count() * 2

        normalized_score = score / maximal_possible_score * 100

        self.score = normalized_score

        self.save()


class Answer(models.Model):
    class AnswerChoice(models.TextChoices):
        ZERO = "0", _("Zero point answer")
        ONE = "1", _("One point answer")
        TWO = "2", _("Two points answer")
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    option = models.CharField(max_length=255, null=True, blank=True, choices=AnswerChoice.choices)
    other = models.TextField(null=True, blank=True)


class Text(models.Model):
    body = models.TextField(verbose_name=_("body"))
    title = models.CharField(verbose_name=_("title"), max_length=255)
    notes = models.TextField(verbose_name=_("notes"))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(verbose_name=_("slug"))
