from django.shortcuts import render, redirect
import json
from datetime import datetime
from django.http import JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.http import Http404
from django.urls import reverse_lazy
from . import forms as u_forms
from accounts import forms as a_forms
from django.views.decorators.csrf import csrf_exempt
from dashboard import models
from django.db.models import Q

# USER ROLE - PERMISSION
from dashboard.decorators import admin_only
from django.utils.decorators import method_decorator

User = get_user_model()

@method_decorator(admin_only, name="dispatch")
class UserListView(LoginRequiredMixin, generic.ListView):
    template_name = 'users/list.html'
    def get_queryset(self):
        try:
            self.user_list = User.objects.raw('SELECT * FROM auth_user AS u INNER JOIN dashboard_profile AS p ON u.id = p.user_id WHERE p.deleted=False')
        except User.DoesNotExist:
            raise Http404
        else:
            return self.user_list

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_list'] = self.user_list
        return context

@login_required
@admin_only
def create_user_profile(request):
    if request.method == 'POST':
        u_form = u_forms.UserCreateForm(request.POST)
        p_form = a_forms.UserProfileForm(request.POST, request.FILES)

        if u_form.is_valid() and p_form.is_valid():
            p_instance = p_form.save(commit=False)
            u_instance = u_form.save(commit=True)
            # user = User.object.filter(id=""+u_instance.cleaned_data['id']).first()

            # profile = user.profile
            p_instance.user = u_instance
            p_instance.save()
            # profile.modified_at = datetime.now()
            # profile.save()
            messages.success(request, "Хэрэглэгч амжилттай бүртгэгдлээ")
            return redirect('users:user_create')
    else:
        u_form = u_forms.UserCreateForm
        p_form = a_forms.UserProfileForm

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/create.html', context)


@login_required
@admin_only
def delete_user_view(request):
    if request.method == "POST":
        id = request.POST.get("id")
        user = User.objects.filter(id=id).first()
        profile = user.profile
        profile.deleted = True
        user.is_active = False
        user.save()
        profile.save()
        return redirect('users:list')
    else:
        return redirect('users:list')

@login_required(login_url="login")
@admin_only
def update_user_view(request):
    pass

class UserMessageView(LoginRequiredMixin, generic.ListView):
    def get_queryset(self):
        return self.request.user
    template_name = "users/messages.html"

    def get_context_data(self, **kwargs):
        notiflist = []
        context = super().get_context_data(**kwargs)
        devices =  models.Device.objects.filter(owner=self.request.user).all()
        for item in devices:
            notif = models.DeviceAndNotification.objects.filter(device=item).all()
            if type(notif.first()).__name__ != "NoneType":
                if len(notif) > 1:
                    for notfItem in notif:
                        if notfItem.first().notification.color == "Blue" or notfItem.first().notification.color == "Green" or notfItem.first().notification.color == "Orange" or notif.first().notification.color == "Orange":
                            notiflist.append(notif.first())
                else:
                    if notif.first().notification.color == "Blue" or notif.first().notification.color == "Green" or notif.first().notification.color == "Orange" or notif.first().notification.color == "Orange":
                        notiflist.append(notif.first())
        context["devices"] = devices
        context["notifications"] = notiflist
        return context


class UserAlertView(LoginRequiredMixin, generic.ListView):
    def get_queryset(self):
        return self.request.user
    template_name = "users/alerts.html"

    def get_context_data(self, **kwargs):
        notiflist = []
        context = super().get_context_data(**kwargs)
        devices =  models.Device.objects.filter(owner=self.request.user).all()
        for item in devices:
            notif = models.DeviceAndNotification.objects.filter(device=item).all().order_by("-created_at")
            if type(notif.first()).__name__ != "NoneType":
                if (len(notif) > 1):
                    for notfItem in notif:
                        if notfItem.notification.color == "Red":
                            notiflist.append(notfItem)
                else:
                    if notif.first().notification.color == "Red":
                        notiflist.append(notif.first())
        print(notiflist)
        context["notifications"] = notiflist
        return context

# class CreateUserView(LoginRequiredMixin, generic.CreateView):
#     template_name = "users/create2.html"
#     form_class = u_forms.UserCreateForm
#     success_url = reverse_lazy("users:user_create")
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['profile_form'] = u_forms.UserProfileForm
#         return context
#     def post(self, request, *args, **kwargs):
#         ctxt = {}
#         print("POST: " + str(request.POST))

# def calculate_age(born):
#     today = datetime.datetime.today()
#     try: # raised when birth day is February 29 and the current year is not a leap year
#         birthday = born.replace(year=today.year)
#     except ValueError:
#         birthday = born.replace(year=today.year, day=born.day-1)

# import pdb; pdb.set_trace();
#
# if birthday > today:
#     return today.year - born.year -1
# else:
#     return today.year - born.year
