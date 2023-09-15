from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

# from django.template import loader

# Class-Based Views
# Generic Class-Based Views
# Function-Based views
"""
def homePageView(request):
    template = loader.get_template("pages/home.html")
    return HttpResponse(template.render())
"""


class HomePageView(TemplateView):
    template_name = "home.html"


class AboutPageView(TemplateView):
    template_name = "about.html"
