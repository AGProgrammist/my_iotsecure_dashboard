from django.http import JsonResponse
import json
from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.http import Http404
from django.urls import reverse_lazy
from users import forms as u_forms
from . import forms as a_forms
from devices import forms as d_forms
from dashboard import models

User = get_user_model()

class ProfileView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'accounts/profile.html'
    model = User
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['u_form'] = u_forms.UserCreateForm
        context['p_form'] = a_forms.UserProfileForm
        context['pchange_form'] = PasswordChangeForm(self.model)
        return context

@login_required()
def update_profile(request):
    if request.method == "POST":
        data = request.POST.get("data")
        dict_data=json.loads(data)
    try:
        user = User.objects.filter(username=dict_data["username"]).first()
        profile = models.Profile.objects.filter(identity_num=dict_data['reg_num']).first()

        profile.firstname = dict_data["firstname"]
        profile.lastname = dict_data["lastname"]
        profile.address = dict_data["address"].replace('ү','v')
        profile.gender = dict_data["gender"]
        profile.phone_num = dict_data["phone_num"]
        profile.identity_num = dict_data["reg_num"]

        profile.save()

        response = {"message": "Хувийн мэдээлэл амжилттай шинэчлэгдлээ!", "error": False}
        return JsonResponse(response, safe=False)
    except:
        response = {"message": "Оруулсан өгөгдлөө шалгана уу!", "error": True}
        return JsonResponse(response, safe=False)

@login_required
def change_password_view(request):
    if request.method == "POST":
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, "Нууц үг амжилттай шинэчлэгдлээ!")
            return redirect('accounts:password_changed')
        else:
            messages.error(request, "Нууц үгээ зөв оруулна уу!")
            return redirect("accounts:user_profile")

@login_required
def change_email_view(request):
    if request.method == "POST":
        data = request.POST.get("data")
        dict_data=json.loads(data)
    try:
        user = User.objects.filter(username=dict_data["username"]).first()
        if (user.email == dict_data['old_email']):
            if (dict_data['new_email'] == dict_data['conf_email']):
                user.email = dict_data['new_email']
                user.save()
                response = {"message": "И-мэйл хаяг амжилттай шинэчлэгдлээ!", "error": False}
            else:
                response = {"message": "Баталгаажуулах и-мэйл хаягаа зөв оруулна уу!", "error": True}
        else:
            response = {"message": "Хуучин и-мэйл хаяг буруу байна!", "error": True}
        return JsonResponse(response, safe=False)
    except:
        response = {"message": "Оруулсан өгөгдлөө шалгана уу!", "error": True}
        return JsonResponse(response, safe=False)

# ТӨХӨӨРӨМЖИД КОМАНД ӨГӨХ 'VIEW' ФУНКЦ
@login_required(login_url="accounts:login")
def remote_device(request):
    if request.method == "POST":
        data = request.POST.get("data")
        dict_data=json.loads(data)
        ucommand = models.Command.objects.filter(code=dict_data["command"]).first()
        uuser = User.objects.filter(id=dict_data["user_id"]).first()
        device = models.Device.objects.filter(code=dict_data["code"]).first()
        print(type(ucommand))
        print(type(uuser))
    try:
        if dict_data["command"] == "devOn":
            models.Device.objects.filter(code=str(dict_data["code"])).update(isActive=True)
            newCommandExec = models.UserAndCommand(command=ucommand, user=uuser)
            newDeviceCommand = models.DeviceAndCommand(command=ucommand, device=device)
            newCommandExec.save()
            newDeviceCommand.save()
        elif dict_data["command"] == "deOff":
            models.Device.objects.filter(code=str(dict_data["code"])).update(isActive=False)
            newCommandExec = models.UserAndCommand(command=ucommand, user=uuser)
            newDeviceCommand = models.DeviceAndCommand(command=ucommand, device=device)
            newCommandExec.save()
            newDeviceCommand.save()
        else:
            newCommandExec = models.UserAndCommand(command=ucommand, user=uuser)
            newDeviceCommand = models.DeviceAndCommand(command=ucommand, device=device)
            newCommandExec.save()
            newDeviceCommand.save()
        #Үргэлжлүүлэх
        response = {"message": "{} комманд амжилттай".format(ucommand.name), "error": False}
        return JsonResponse(response, safe=False)
    except:
        response = {"message": "Оролдлого амжилтгүй!", "error": True}
        return JsonResponse(response, safe=False)

class MyDevicesList(LoginRequiredMixin, generic.ListView): # REPLACE TO ListView
    template_name = "accounts/devices.html"

    def get_queryset(self):
        self.device_list = models.Device.objects.filter(owner_id=self.request.user.id, deleted=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['device_list'] = self.device_list
        context['d_form'] = d_forms.UpdateDeviceForm
        return context
