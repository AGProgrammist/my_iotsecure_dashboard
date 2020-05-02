from django import template
from dashboard import models
from django.db.models import Count
from django.contrib.auth import get_user_model
from datetime import datetime
from dashboard.models import Device, DeviceAndNotification

User = get_user_model()
register = template.Library()

@register.filter(name="getObjectCount")
def getObjectCount(value):
    """
    Бүртгэлтэй төхөөрөмжүүд эсвэл хэрэглэгчдийг тоолох
    return integer - төхөөрөмжийн тоо эсвэл хэрэглэгчийн тоо
    """
    if value == "user" or value == "User":
        user_list = User.objects.raw('SELECT * FROM auth_user AS u INNER JOIN dashboard_profile AS p ON u.id = p.user_id WHERE p.deleted=False')
        return len(user_list)
    elif value == "device" or value == "Device":
        device_count = models.Device.objects.filter(deleted=False)
        return len(device_count)
    else:
        return 0

@register.filter(name="getUserCount")
def getUserCount(month):
    """
    Тухайн сард бүртгүүлсэн хүний тоог харуулна.
    """
    today = datetime.now()

    user_list = User.objects.raw('SELECT * FROM auth_user AS u ' +
                                'INNER JOIN dashboard_profile AS p ' +
                                'ON u.id = p.user_id WHERE p.deleted=False ' +
                                'AND YEAR(p.created_at) = ' + str(today.year) +
                                ' AND MONTH(p.created_at) = ' + month)
    return len(user_list)
@register.filter(name="getDeviceCountMonth")
def getDeviceCountMonth(month):
    """
    Тухайн сард бүртгэсэн төхөөрөмжийн тоог буцаана.
    """
    today = datetime.now()

    device_list = Device.objects.raw('SELECT * FROM dashboard_device' +
                                    ' WHERE deleted=False ' +
                                    'AND YEAR(created_at) = ' + str(today.year) +
                                    ' AND MONTH(created_at) = ' + month)
    return len(device_list)

@register.filter(name="getDeviceCount")
def getDeviceCount(u_id):
    """
    Тухайн хэрэглэгчийн нийт төхөөрөмжийн тоог буцаана.
    """
    devices = Device.objects.filter(owner_id = int(u_id))

    return len(devices)

@register.filter(name="getAlertCount")
def getAlertCount(u_id):
    """
    Тухайн хэрэглэгчид ирсэн нийт анхааруулга мэдэгдлийн тоог харуулна.
    """
    counter = 0
    devices = Device.objects.filter(owner_id = int(u_id))
    for item in devices:
        # Анхааруулга мэдэгдлийн id = 1
        alert = DeviceAndNotification.objects.filter(device_id=item.code, notification_id=1)
        counter = counter + len(alert)
    return counter

@register.filter(name="getCommonMsgCount")
def getCommonMsgCount(u_id):
    """
    Тухайн хэрэглэгчид ирсэн нийт энгийн мэдэгдэлийн тоог харуулна.
    """
    counter = 0
    devices = Device.objects.filter(owner_id = int(u_id))
    for item in devices:
        # id = 2
        alert = DeviceAndNotification.objects.filter(device_id=item.code, notification_id=2)
        counter = counter + len(alert)
    return counter

@register.filter(name="getCurrentUserDevices")
def getCurrentUserDevices(u_id):
    """
    params: u_id - хэрэглэгчийн дугаар
    Тухайн хэрэглэгч дээр бүртгэлтэй төхөөрөмжүүдийн кодыг буцаана.
    """
    device_names = Device.objects.values_list("code", flat=True).filter(owner_id = int(u_id))
    return device_names
