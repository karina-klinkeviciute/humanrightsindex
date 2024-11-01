from modeltranslation.translator import TranslationOptions, translator

from models import Weight, Question


class WeightTranslationOptions(TranslationOptions):
    fields = ('weight_question', )


class QuestionTranslationOptions(TranslationOptions):
    fields = ('question', 'answer_0_points', 'answer_1_points', 'answer_2_points', )


translator.register(Weight, WeightTranslationOptions)
translator.register(Question, QuestionTranslationOptions)
