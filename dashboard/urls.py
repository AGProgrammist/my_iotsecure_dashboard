from django.urls import path
from . import views

app_name = "dashboard"
urlpatterns = [
    path('', views.DashboardHomeView.as_view(), name="home"),
    path('alert_graph', views.getDeviceAlertCountMonth, name="alert_month"),
]
