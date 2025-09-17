from django.shortcuts import render
from django.views.generic import TemplateView

class PrivacyPolicyView(TemplateView):
    template_name = 'privacy_policy.html'