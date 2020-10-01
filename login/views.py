from django.shortcuts import render
from django.views import generic 
from django.shortcuts import redirect 
from django.views.generic.base import TemplateResponseMixin 

from PrintSystem.mixins import RequireLoginMixin 

""" class IndexView(RequireLoginMixin, generic.ListView): 
    template_name       = ".html"
    context_object_name = ""
    
    def def get_queryset(self): 
        return super().get_queryset()
    
class ResultsView(TemplateResponseMixin, generic.View): 
    template_name = ".html"
        
    def get_queryset(self, questionId): 
        return Question.objects.get(pk=questionId)
    
    def get(self, request, pk): 
        queryset = self.get_queryset(pk)
        context  = {'question': queryset}
        return self.render_to_response(context) 

class SwitchboardView(generic.View): 
def   get(self, request, pk)       : 
        view = ResultsView.as_view()
        return view(request, pk) 
    
    def post(self, request, pk): 
        view = VoteView.as_view()
        return view(request, pk) 
    
     """