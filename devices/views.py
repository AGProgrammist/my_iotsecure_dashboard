from django.shortcuts import render, redirect
import json
from datetime import datetime
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views import generic
from dashboard.models import Device, DeviceTypeRef
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from . import forms
from dashboard import models

# USER ROLE - PERMISSION
from dashboard.decorators import admin_only
from django.utils.decorators import method_decorator

class DeviceListView(LoginRequiredMixin, generic.ListView): # REPLACE TO ListView
    template_name = "devices/list.html"

    def get_queryset(self):
        self.device_list = Device.objects.filter(deleted=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['device_list'] = self.device_list
        context['d_form'] = forms.UpdateDeviceForm
        return context

@method_decorator(admin_only, name="dispatch")
class DeviceCreateView(LoginRequiredMixin, generic.CreateView):
    template_name = "devices/create.html"
    form_class = forms.CreateDeviceForm

    def get_queryset(self):
        if self.request.method == "POST":
            print("hello")
        else:
            print("HELLLEELLLELLELELLELELELLE")
        messages.error(self.request, "Амжилттай")
        print("helelo")

@login_required()
@admin_only
def update_device(request):
    if request.method == "POST":
        d_form = forms.UpdateDeviceForm(request.POST, request.FILES)
        if d_form.is_valid():
            device = models.Device.objects.filter(code=request.POST.get("dev_code")).first()

            device.name = d_form.cleaned_data["name"]
            device.image = d_form.cleaned_data["image"]
            device.owner = d_form.cleaned_data["owner"]
            device.modified_at = datetime.now()
            device.save()
            messages.error(request, "Амжилттай")
            return redirect("devices:list")
        else:
            print(request.POST.get("dev_code"))
            messages.error(request, "Алдаа")
            return redirect("devices:list")

@login_required
@admin_only
def delete_device_view(request):
    if request.method == "POST":
        code = request.POST.get('code')
        device = Device.objects.filter(code=code).first()
        device.deleted = True
        device.save()
        return redirect("devices:list")
    else:
        return redirect("devices:list")
