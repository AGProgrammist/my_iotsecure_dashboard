from django.urls import path
from . import views

app_name = 'users'
urlpatterns = [
    path('list/', views.UserListView.as_view(), name='list'),
    path('create/', views.create_user_profile, name='user_create'),
    path('delete/', views.delete_user_view, name="delete"),
    path('update/', views.update_user_view, name="update"),
    path('messages/', views.UserMessageView.as_view(), name="messages"),
    path('alerts/', views.UserAlertView.as_view(), name="alerts"),
    path('delete_a/<int:pk>', views.delete_notif_alert, name="deleteAlert"),
    path('delete_c/<int:pk>', views.delete_notif_common, name="deleteCommon"),
]
