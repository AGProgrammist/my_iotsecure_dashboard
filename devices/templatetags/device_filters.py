from django import template
register = template.Library()
from dashboard.models import Device

@register.filter(name='toString')
def toString(value):
    return str(value)

@register.filter(name="getDeviceImgUrl")
def getDeviceImgUrl(dev_code):
    pass
    # device = Device.objects.filter(code=dev_code).first()
    # return device.image.url
