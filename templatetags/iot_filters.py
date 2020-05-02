from django import template
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
        device_list = models.Device.objects.filter(deleted=False)
        return len(device_list)

@register.filter(name="getCurrentUserField")
def getCurrentUsername(user, arg):
    """
    Нэвтэрсэн хэрэглэгчийн field_name буюу талбарын утгыг буцаана
    """
