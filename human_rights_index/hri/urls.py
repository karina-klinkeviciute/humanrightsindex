from django.urls import path

from .views import EnterGroupCodeView, SurveyView, CompleteView, IndexView, WeightView, \
    GroupCreateView, GroupSearchView, AboutView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('enter-group-code/', EnterGroupCodeView.as_view(), name='enter_group_code'),
    path('survey/<int:survey_id>/<int:question_number>/', SurveyView.as_view(), name='survey'),
    path('survey/<int:survey_id>/complete/', CompleteView.as_view(), name='survey_complete'),
    path('survey/<int:survey_id>/weight/', WeightView.as_view(), name='weight'),
    path('create-group/', GroupCreateView.as_view(), name='create_group'),
    path('search-group/', GroupSearchView.as_view(), name='search_group'),
    path('about/', AboutView.as_view(), name='about'),
]
