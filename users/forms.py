from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from dashboard.models import Profile
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator
import datetime

class UserCreateForm(UserCreationForm):
    class Meta:
        fields = ('username', 'email', 'password1', 'password2')
        model = get_user_model()
        error_messages = {
            'username' : {
                'required' : _("Хэрэглэгчийн нэрээ оруулна уу!")
            }
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Хэрэглэгчийн нэр *'
        self.fields['email'].label = 'И-мэйл хаяг *'
        self.fields['password1'].label = 'Нууц үг *'
        self.fields['password2'].label = 'Баталгаажуулах нууц үг *'


# class UpdateEmailForm(forms.ModelForm):
#     class Meta:
#         fields = ('email', 'password1', 'password2')
#         model = get_user_model()
#         error_messages = {
#             'username' : {
#                 'required' : _("Хэрэглэгчийн нэрээ оруулна уу!")
#             }
#         }
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['email'].label = 'И-мэйл хаяг'
#         self.fields['password1'].label = 'Нууц үг'
#         self.fields['password2'].label = 'Баталгаажуулах нууц үг'

class UserProfileForm(forms.ModelForm):
    address = forms.CharField(widget=forms.Textarea(attrs={"rows":5, "cols":20}))
    # phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    # phone_num = forms.CharField(validators=[phone_regex])

    class Meta():
        model = Profile
        fields = "__all__"
        labels = {
            'lastname': _('Овог*'),
            'firstname': _('Нэр*'),
            'image': _('Зураг'),
            'identity_num': _('Регистрийн дугаар*'),
            'birth': _('Төрсөн огноо*'),
            'gender': _('Хүйс*'),
            'phone_num': _('Утасны дугаар*'),
            'address': _('Гэрийн хаяг')
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['birth'].label = 'Төрсөн огноо *'
        self.fields['address'].label = 'Гэрийн хаяг'
