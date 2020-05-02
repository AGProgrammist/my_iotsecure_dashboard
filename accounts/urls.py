from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'accounts'
urlpatterns = [
    path('login/',
        auth_views.LoginView.as_view(template_name='accounts/login.html', redirect_authenticated_user=True),
        name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('update/', views.update_profile, name="update"),
    path('profile/', views.ProfileView.as_view(), name='user_profile'),
    path('change-password/', views.change_password_view, name="change_password"),
    path('password-changed/', views.ProfileView.as_view(), name="password_changed"),
    path('change-email/', views.change_email_view, name="change_email"),
    path('email-changed/', views.ProfileView.as_view(), name="email_changed"),
    path('my-devices/', views.MyDevicesList.as_view(), name="my_devices"),
    path('remote-device/', views.remote_device, name="remote_device"),
]
