from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
class HomePage(LoginRequiredMixin, TemplateView):
    template_name = "dashboard/index.html"
    login_url = "accounts:login"
