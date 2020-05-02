from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from dashboard import models

User = get_user_model()

class DashboardHomeView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard/index.html'
    login_url = 'accounts:login'
    # try:
    #     user_list = User.objects.raw('SELECT * FROM auth_user AS u INNER JOIN dashboard_profile AS p ON u.id = p.user_id WHERE p.deleted=False')
    #     device_list = models.Device.objects.filter(deleted=False)
    # except User.DoesNotExist:
    #     raise Http404
    #
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #
    #     context['count_users'] = (len(self.user_list))
    #     context['count_devices'] = (len(self.device_list))
    #     return context
