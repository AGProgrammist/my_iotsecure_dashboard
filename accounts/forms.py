from django import forms
from django.contrib.auth import get_user_model
from dashboard.models import Profile
from django.utils.translation import gettext_lazy as _
import datetime

class UserProfileForm(forms.ModelForm):
    address = forms.CharField(widget=forms.Textarea(attrs={"rows":5, "cols":20}))

    class Meta():
        model = Profile
        fields = "__all__"
        labels = {
            'lastname': _('Овог *'),
            'firstname': _('Нэр *'),
            'image': _('Зураг'),
            'identity_num': _('Регистрийн дугаар *'),
            'gender': _('Хүйс *'),
            'phone_num': _('Утасны дугаар *'),
            'address': _('Гэрийн хаяг')
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['birth'].label = 'Төрсөн огноо'
        self.fields['address'].label = 'Гэрийн хаяг'
