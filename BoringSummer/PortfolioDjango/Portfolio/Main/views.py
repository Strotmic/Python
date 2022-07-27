from django.shortcuts import render
from django.views.generic import * 
from Main.models import *

class IndexView(TemplateView):
    template_name = "Main/index.html"

class BlogListView(ListView):
    context_object_name = 'blogs'
    model = Blog




# Create your views here.
