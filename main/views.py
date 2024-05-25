from django.shortcuts import render
from django.views import generic


class HomeView(generic.TemplateView):
    template_name = 'index.html'


class AdmissionView(generic.TemplateView):
    template_name = 'admission.html'


class CoursesView(generic.TemplateView):
    template_name = 'courses.html'


class AboutUniView(generic.TemplateView):
    template_name = 'AboutUniversity.html'


class FacultiesView(generic.TemplateView):
    template_name = 'institute.html'


class AdviceView(generic.TemplateView):
    template_name = 'advice.html'


class BachelorsView(generic.TemplateView):
    template_name = 'bachelors.html'


class CollegeView(generic.TemplateView):
    template_name = 'college.html'


class ContactsView(generic.FormView):
    template_name = 'contacts.html'


class CreativeView(generic.TemplateView):
    template_name = 'creative.html'


class DigitalInstituteView(generic.TemplateView):
    template_name = 'digitaiInstitute.html'


class DoctoralView(generic.TemplateView):
    template_name = 'doctoral.html'


class EnactusView(generic.TemplateView):
    template_name = 'enactus.html'


class InstituteConstructionView(generic.TemplateView):
    template_name = 'InstituteConstruction.html'


class InstituteDesignView(generic.TemplateView):
    template_name = 'instituteDesign.html'


class InstituteEconomicsView(generic.TemplateView):
    template_name = 'InstituteEconomics.html'


class InstituteEnergyView(generic.TemplateView):
    template_name = 'instituteEnergy.html'


class InstituteInterculturalView(generic.TemplateView):
    template_name = 'InstituteIntercultural.html'


class InstituteMarketingView(generic.TemplateView):
    template_name = 'InstituteMarketing.html'


class MasterdegreeView(generic.TemplateView):
    template_name = 'mastersDegree.html'


class PostgraduateView(generic.TemplateView):
    template_name = 'postgraduate.html'


class QuestionnaireView(generic.TemplateView):
    template_name = 'questionnaire.html'


class ReceptionView(generic.TemplateView):
    template_name = 'receprtion.html'


class RussianKyrgyzInstituteView(generic.TemplateView):
    template_name = 'russianKyrgyzInstitute.html'


class NewsView(generic.TemplateView):
    template_name = 'uncos.html'
