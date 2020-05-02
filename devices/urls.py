from django.urls import path
from . import views

app_name = 'devices'

urlpatterns = [
    path('list', views.DeviceListView.as_view(), name="list"),
    path('create/', views.DeviceCreateView.as_view(), name="device_create"),
    path('create/<str:id>', views.DeviceCreateView.as_view(), name="device_created"),
    path('delete/', views.delete_device_view, name="delete"),
    path('device-update/', views.update_device, name="update"),
    path('device-update/', views.update_device, name="update"),
]
