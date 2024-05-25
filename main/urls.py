from django.urls import path
from .views import *


urlpatterns = [
    path('', HomeView.as_view()),
    path('admission/', AdmissionView.as_view()),
    path('courses/', CoursesView.as_view()),
    path('about/', AboutUniView.as_view()),
    path('institute/', FacultiesView.as_view()),
    path('advice/', AdviceView.as_view()),
    path('bachelors/', BachelorsView.as_view()),
    path('college/', CollegeView.as_view()),
    path('contacts/', ContactsView.as_view()),
    path('creative/', CreativeView.as_view()),
    path('digitalinstitute/', DigitalInstituteView.as_view()),
    path('doctoral/', DoctoralView.as_view()),
    path('enactus/', EnactusView.as_view()),
    path('instituteconstractiom/', InstituteConstructionView.as_view()),
    path('institutedesign/', InstituteDesignView.as_view()),
    path('instituteeconomics/', InstituteEconomicsView.as_view()),
    path('instituteintercultural/', InstituteInterculturalView.as_view()),
    path('institutemarketing/', InstituteMarketingView.as_view()),
    path('masterdegree/', MasterdegreeView.as_view()),
    path('postgraduate/', PostgraduateView.as_view()),
    path('questionnaire/', QuestionnaireView.as_view()),
    path('reception/', ReceptionView.as_view()),
    path('russiankyrgyz/', RussianKyrgyzInstituteView.as_view()),
    path('news/', NewsView.as_view()),
]
