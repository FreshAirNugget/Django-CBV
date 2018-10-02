from django.shortcuts import render
from django.views.generic import View,TemplateView,DetailView,ListView
from . import models
# Create your views here.

class SchoolListView(ListView):
    model = models.School
    template_name = 'basic_app/school_list.html'

class SchoolDetailView(DetailView):
    model = models.School
    template_name = 'basic_app/school_detail.html'



# class IndexView(TemplateView):
#     template_name = 'basic_app/index.html'
#
#     def get_context_data(self,**kwargs):
#         context = super().get_context_data(**kwargs)
#         context['inject_me'] = 'HEY! I\'M INJECTED'
#         return context
