from django import forms
from dashboard.models import Device
from django.utils.translation import gettext_lazy as _

class CreateDeviceForm(forms.ModelForm):
    class Meta:
        model = Device
        fields = ('code', 'name', 'type', 'owner', 'image')
        labels = {
            'code': _('Код *'),
            'name': _('Нэр *'),
            'type': _('Төрөл *'),
            'owner': _('Эзэмшигч'),
            'image': _('Төхөөрөмжийн зураг')
        }

class UpdateDeviceForm(forms.ModelForm):
    class Meta:
        model = Device
        fields = ('name', 'type', 'owner', 'image')
        labels = {
            'name': _('Нэр'),
            'type': _('Төрөл'),
            'owner': _('Эзэмшигч'),
            'image': _('Төхөөрөмжийн зураг')
        }




    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['code'].label = 'Код'
    #     self.fields['name'].label = 'Нэр'
    #     self.fields['type'].label = 'Төрөл'
    #     self.fields['owner'].label = 'Эзэмшигч'
    #     self.fields['image'].label = 'Зураг'
