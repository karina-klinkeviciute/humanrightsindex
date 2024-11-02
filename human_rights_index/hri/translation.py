from modeltranslation.translator import TranslationOptions, translator

from hri.models import Weight, Question, Text


class WeightTranslationOptions(TranslationOptions):
    fields = ('weight_question', )


class QuestionTranslationOptions(TranslationOptions):
    fields = ('question', 'answer_0_points', 'answer_1_points', 'answer_2_points', )


class TextTranslationOptions(TranslationOptions):
    fields = ('body', 'title', 'notes')


translator.register(Weight, WeightTranslationOptions)
translator.register(Question, QuestionTranslationOptions)
translator.register(Text, TextTranslationOptions)
