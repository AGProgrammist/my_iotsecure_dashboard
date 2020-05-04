from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from dashboard import models
import json
from datetime import datetime

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

# def getDeviceAlertCountMonth(request):
#     if request.method == "POST":
#         data = request.POST.get("data")
#         dict_data=json.loads(data)
#         today = datetime.now()
#
#         try:
#             counter = 0
#             devices = models.Device.objects.filter(code=dict_data["dev_code"])
#
#             # Сар бүрийн анхааруулга мэдэгдэл
#             if (dict_data["type"] == "all"):
#                 for item in devices:
#                     # Анхааруулга мэдэгдлийн id = 1
#                     # Тухайн төхөөрөмжөөс ирсэн анхааруулга мэдэгдэлийг шүүх
#                     alert = models.DeviceAndNotification.objects.raw("SELECT MONTH(created_at), COUNT(device_id) as num FROM dashboard.DeviceAndNotification AS dale "
#                                                                      + " device_id = " + item.code + " YEAR(created_at) = "
#                                                                      + today.year + " GROUP BY MONTH(created_at)")
#                     alert = models.DeviceAndNotification.objects.filter(device_id=item.code, notification_id=1)
#                     today = datetime.now()

#                    if alert.created_at.year == today.year and alert:
#                        counter = counter + len(alert)
