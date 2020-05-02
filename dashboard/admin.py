from django.contrib import admin
from dashboard import models as m

admin.site.register(m.DeviceTypeRef)
admin.site.register(m.EMailTypeRef)
admin.site.register(m.DeviceMode)
admin.site.register(m.DeviceState)
admin.site.register(m.Command)
admin.site.register(m.DeviceNotification)
admin.site.register(m.Profile)
admin.site.register(m.Device)
admin.site.register(m.DeviceAndCommand)
admin.site.register(m.UserAndCommand)
admin.site.register(m.DeviceAndState)
admin.site.register(m.DeviceAndMode)
admin.site.register(m.DeviceAndEmail)
admin.site.register(m.DeviceAndNotification)
