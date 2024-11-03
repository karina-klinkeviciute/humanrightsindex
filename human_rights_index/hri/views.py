from django.shortcuts import redirect, render

from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import FormView, View, TemplateView, CreateView

from .forms import GroupCodeForm, SurveyAnswerForm, WeightForm, GroupForm, GroupSearchForm
from .models import Group, Survey, Question, Answer, Weight, Text


class IndexView(TemplateView):
    template_name = 'hri/index.html'


class EnterGroupCodeView(FormView):
    """ View to handle the group code entry. """
    template_name = 'hri/enter_group_code.html'
    form_class = GroupCodeForm

    def form_valid(self, form):
        code = form.cleaned_data.get('code')

        if code:
            # If a code is provided, find the group and create a new survey linked to it
            group = get_object_or_404(Group, code=code)
            survey = Survey.objects.create(group=group)
        else:
            # Create a survey without any group association
            survey = Survey.objects.create()  # No group linked

        # Redirect to the survey page with the new survey's ID
        return redirect('survey', survey_id=survey.id, question_number=1)


class SurveyView(View):
    def get(self, request, survey_id, question_number):
        survey = get_object_or_404(Survey, id=survey_id)
        questions = Question.objects.all()

        if question_number < 1 or question_number > questions.count():
            return redirect('survey_complete', survey_id=survey_id)

        question = questions[question_number - 1]  # 0-based index for question

        # Pass the question to the form to dynamically populate answer labels
        form = SurveyAnswerForm(question=question)

        return render(request, 'hri/survey.html', {
            'survey': survey,
            'question': question,
            'question_number': question_number,
            'total_questions': questions.count(),
            'form': form
        })

    def post(self, request, survey_id, question_number):
        survey = get_object_or_404(Survey, id=survey_id)
        questions = Question.objects.all()

        question = questions[question_number - 1]  # 0-based index for question

        form = SurveyAnswerForm(request.POST, question=question)  # Pass question to form

        if form.is_valid():
            selected_answer = form.cleaned_data['answer']
            Answer.objects.update_or_create(
                survey=survey,
                question=question,
                option=selected_answer
            )

            # Move to the next question or redirect to completion page
            if question_number < questions.count():
                return redirect('survey', survey_id=survey_id, question_number=question_number + 1)
            else:
                return redirect('weight', survey_id=survey_id)

        return render(request, 'hri/survey.html', {
            'survey': survey,
            'question': question,
            'question_number': question_number,
            'total_questions': questions.count(),
            'form': form
        })


class WeightView(View):
    def get(self, request, survey_id):
        survey = get_object_or_404(Survey, id=survey_id)
        form = WeightForm()
        return render(request, 'hri/weight.html', context={'survey': survey, 'form': form})

    def post(self, request, survey_id):
        survey = get_object_or_404(Survey, id=survey_id)
        form = WeightForm(request.POST)
        if form.is_valid():
            weight = form.cleaned_data['weight_choice']
            weight_item = Weight.objects.get(id=weight)
            survey.weight = weight_item
            survey.save()

        return redirect('survey_complete', survey_id=survey_id)


class CompleteView(View):
    def get(self, request, survey_id):
        survey = get_object_or_404(Survey, id=survey_id)
        survey.calculate_score()
        group = survey.group
        if group and group.survey_set.count() > 5:
            group.calculate_score()
        else:
            group = None
        return render(request, 'hri/survey_complete.html', {'survey': survey, "group": group})


class GroupCreateView(CreateView):
    model = Group
    form_class = GroupForm
    template_name = 'hri/create_group.html'

    # Override form_valid to pass the created group to the success page
    def form_valid(self, form):
        # Save the form to create the Group instance
        self.object = form.save()

        # Instead of redirecting immediately, render the success page with the group info
        return render(self.request, 'hri/create_group_success.html', {'group': self.object})


class GroupSearchView(CreateView):
    form_class = GroupSearchForm
    template_name = 'hri/search_group.html'

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        group = None
        if form.is_valid():
            code = form.cleaned_data['code']

            try:
                # Try to fetch the group with the provided code
                group = Group.objects.get(code=code)
            except Group.DoesNotExist:
                form.add_error('code', 'Group with this code does not exist.')

        return render(request, self.template_name, {'form': form, 'group': group})

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})


class TextView(TemplateView):
    template_name = 'hri/text.html'

    def get_context_data(self, slug, **kwargs):
        text = Text.objects.get(slug=slug)
        return {'text': text}
