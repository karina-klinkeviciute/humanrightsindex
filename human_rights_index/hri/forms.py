import re

from django import forms

from hri.models import Weight, Group
from django.utils.translation import gettext_lazy as _


class GroupCodeForm(forms.Form):
    code = forms.CharField(max_length=255, required=False, label=_('Enter Group Code'))


class SurveyAnswerForm(forms.Form):
    answer = forms.ChoiceField(widget=forms.RadioSelect, label=_("Select your answer"))

    def __init__(self, *args, **kwargs):
        # Get the question instance passed in through the view
        question = kwargs.pop('question', None)
        super(SurveyAnswerForm, self).__init__(*args, **kwargs)

        # Dynamically set the choices based on the question's answers
        if question:
            choices = []
            if question.answer_0_points:
                choices.append(('0', question.answer_0_points))
            if question.answer_1_points:
                choices.append(('1', question.answer_1_points))
            if question.answer_2_points:
                choices.append(('2', question.answer_2_points))
            self.fields['answer'].choices = choices


class WeightForm(forms.Form):
    weight_choice = forms.ChoiceField(
        choices=[],  # We'll populate this dynamically
        widget=forms.RadioSelect,  # This renders it as radio buttons
        label=_("In your own life, which of those factors has the biggest impact on your vulnerability?")
    )

    def __init__(self, *args, **kwargs):
        super(WeightForm, self).__init__(*args, **kwargs)
        # Dynamically populate the choices from the Weight model
        self.fields['weight_choice'].choices = [
            (weight.id, weight.weight_question) for weight in Weight.objects.all()
        ]


class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['name', 'code']

    def clean_code(self):
        code = self.cleaned_data.get('code')

        # Ensure the code is at least 7 characters long
        if len(code) < 7:
            raise forms.ValidationError(_("Group code has to be at least 7 characters long."))

        # Ensure the code contains only letters and numbers
        if not re.match(r'^[A-Za-z0-9]+$', code):
            raise forms.ValidationError(_("Code can only have letters and numbers"))

        # Check if the code already exists in the database
        if Group.objects.filter(code=code).exists():
            raise forms.ValidationError(_("A group with this code already exists. Please enter a different code"))

        return code


class GroupSearchForm(forms.Form):
    code = forms.CharField(max_length=255, label=_("Enter Group Code"))

    # You can add further validation if needed (e.g., regex for alphanumeric characters)
    def clean_code(self):
        code = self.cleaned_data.get('code')

        if not code:
            raise forms.ValidationError(_("Please enter a valid group code."))

        return code

