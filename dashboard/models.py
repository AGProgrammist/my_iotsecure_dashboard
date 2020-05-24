from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User
from django.urls import reverse
from phonenumber_field.modelfields import PhoneNumberField
from PIL import Image
from datetime import datetime

class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(default=datetime.now, blank=True, null=True)
    modified_at = models.DateTimeField(blank=True, null=True)
    deleted = models.BooleanField(default=False, null=True, blank=True)
    class Meta:
        abstract = True
        ordering = ['-created_at']

# Төхөөрөмжийн төрлийн лавлах
class DeviceTypeRef(TimeStampedModel):
    """
    Төхөөрөмжийн төрөл
    """
    code = models.CharField(max_length=5, primary_key=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return "{} - {}".format(self.code, self.name)

# Мэйл зурвасын төрлийн лавлах
class EMailTypeRef(TimeStampedModel):
    """
    Мэйл зурвасын төрлийн лавлах
    """
    code = models.CharField(max_length=4, primary_key=True)
    name = models.CharField(max_length=80)

    def __str__(self):
        return "{} - {}".format(self.code, self.name)

# Горим
class DeviceMode(TimeStampedModel):
    """
    Горим
    """
    code = models.CharField(max_length=4, primary_key=True)
    name = models.CharField(max_length=30)

    def __str__(self):
        return "{} - {}".format(self.code, self.name)

# Төлөв
class DeviceState(TimeStampedModel):
    """
    Төлөв
    """
    code = models.CharField(max_length=4, primary_key=True)
    name = models.CharField(max_length=45)

    def __str__(self):
        return "{} - {}".format(self.code, self.name)

# Команд
class Command(TimeStampedModel):
    """
    Команд
    """
    code = models.CharField(max_length=5, primary_key=True)
    name = models.CharField(max_length=45)

    def __str__(self):
        return "{} - {}".format(self.code, self.name)

# Мэдэгдэл
class DeviceNotification(TimeStampedModel):
    """
    Мэдэгдэл
    """
    RED = 'Red'
    YELLOW = "Yellow"
    GREEN = "Green"
    BLUE = "Blue"
    ORANGE = "Orange"

    COLOR_CHOICES = [
        (RED, 'Улаан'),
        (YELLOW, 'Шар'),
        (GREEN, 'Ногоон'),
        (BLUE, 'Цэнхэр'),
        (ORANGE, 'Улбар шар')
    ]

    name = models.CharField(max_length=20, blank=False, null=False, unique=True)
    color = models.CharField(max_length=15, choices=COLOR_CHOICES, default=GREEN)

    def __str__(self):
        return "{} - {}".format(self.name, self.color)


# Хэрэглэгч - Хэрэглэгчийн профайл
class Profile(TimeStampedModel):
    """
    Хэрэглэгчийн профайл
    Уг модель нь User модельтэй 1:1 холбоосоор холбогдсон
    """
    MALE = "Эр"
    FEMALE = "Эм"
    GenderChoices = [
        (MALE, "Эрэгтэй"),
        (FEMALE, "Эмэгтэй")
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    lastname = models.CharField(max_length=100)
    firstname = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/profile_pictures', default='images/default_profile.png', null=True, blank=True)
    # Регистрийн дугаар
    identity_num = models.CharField(max_length=10, unique=True)
    birth = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=2, choices=GenderChoices, default=MALE)
    phone_num = models.CharField(max_length=11)
    address = models.TextField(max_length=255, null=True, blank=True)

    def __str__(self):
        return "{} - {}, Идэвхгүй: {}".format(self.identity_num, self.firstname, self.deleted)

    def get_absolute_url(self):
        return reverse("users:user_created", kwargs={"username":self.user.username})

    def save(self):
        """
        Зургийг 200:200 хэмжээтэйгээр хадгална.
        """
        super().save()
        img = Image.open(self.image.path)
        if img.height > 200 and img.width > 200:
            output_size = (200, 200)
            img.thumbnail(output_size)
            img.save(self.image.path)

# Төхөөрөмж
class Device(TimeStampedModel):
    """
    Төхөөрөмж
    """
    code = models.CharField(max_length=11, primary_key=True)
    name = models.CharField(max_length=100, default='төхөөрөмж')
    type = models.ForeignKey(DeviceTypeRef, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    image = models.ImageField(upload_to='images/device_pictures', default='images/default_device.png')
    deleted = models.BooleanField(null=True, blank=True, default=False)
    access_token = models.CharField(max_length=255, null=True, blank=True)
    isActive = models.BooleanField(null=True, blank=True)
    def __str__(self):
        return "{} - {}, Идэвхгүй: {}, Эзэмшигч: {}".format(self.type.name, self.name, self.deleted, self.owner)

    def get_absolute_url(self):
        return reverse("devices:device_created", kwargs={"id":self.code})

    def save(self):
        """
        Зургийг 400:400 хэмжээтэйгээр хадгална.
        """
        super().save()
        img = Image.open(self.image.path)
        if img.height > 200 and img.width > 200:
            output_size = (200, 200)
            img.thumbnail(output_size)
            img.save(self.image.path)

# Төхөөрөмж ба команд
class DeviceAndCommand(models.Model):
    """
    Төхөөрөмж ба команд - Төхөөрөмжийн гүйцэтгэсэн команд бүрийг хадгална
    """
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    command = models.ForeignKey(Command, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(default=datetime.now, null=True, blank=True)
    isEnable = models.BooleanField(default=True, null=True, blank=True) #ADDED 2020-05-23, 09:54PM
    def __str__(self):
        return "{} -ийн {} команд: {}".format(self.device.code, self.command.name, self.created_at)

    class Meta:
        ordering = ['-device', '-created_at']

# Хэрэглэгч ба команд
class UserAndCommand(models.Model):
    """
    Хэрэглэгч платформоос төхөөрөмж рүү өгсөн команд бүрийг хадгална
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    command = models.ForeignKey(Command, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(default=datetime.now, blank=True, null=True)

    def __str__(self):
        return "{} -ийн өгсөн {} команд: {}".format(self.user.username, self.command.name, self.created_at)

    class Meta:
        ordering = ['-user', '-created_at']

# Төхөөрөмж ба төлөв
class DeviceAndState(models.Model):
    """
    Төхөөрөмжийн төлөв өөрчлөгдөх үед хадгална
    """
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    state = models.ForeignKey(DeviceState, on_delete=models.SET_NULL, null=True, blank=True)

    created_at = models.DateTimeField(default=datetime.now, blank=True, null=True)

    def __str__(self):
        return "{} -ийн {} төлөв: {}".format(self.device.code, self.state.name, self.created_at)

    class Meta:
        ordering = ['-device', '-created_at']

# Төхөөрөмж ба горим
class DeviceAndMode(models.Model):
    """
    Төхөөрөмжийн горим өөрчлөгдөх үед хадгална
    """
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    mode = models.ForeignKey(DeviceMode, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(default=datetime.now, blank=True, null=True)

    def __str__(self):
        return "{} -ийн {} горим: {}".format(self.device.code, self.mode.name, self.created_at)

    class Meta:
        ordering = ['-device', '-created_at']

# Төхөөрөмж ба и-мэйл зурвас
class DeviceAndEmail(models.Model):
    """
    Төхөөрөмжийн илгээсэн имэйл бүрийг хадгална
    """
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    email = models.ForeignKey(EMailTypeRef, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=100)
    msg_body = models.TextField()

    # АЧААЛЛЫГ ИХЭСГЭХ БОЛ УГ ТАЛБАРЫГ ХАСНА
    image = models.ImageField(null=True, blank=True, upload_to='images/email_pictures')
    created_at = models.DateTimeField(default=datetime.now, null=True, blank=True)

    def __str__(self):
        return "{} -ийн {} горим: {}".format(self.device.code, self.email.name, self.created_at)

    class Meta:
        ordering = ['-device', '-created_at']

# Төхөөрөмж ба мэдэгдэл
class DeviceAndNotification(models.Model):
    """
    Төхөөрөмжөөс ирэх мэдэгдлүүд
    """
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    notification = models.ForeignKey(DeviceNotification, on_delete=models.SET_NULL, null=True, blank=True)
    msg = models.CharField(max_length=1024)

    created_at = models.DateTimeField(default=datetime.now, null=True, blank=True)

    def __str__(self):
        return "{} - {}".format(self.device.code, self.notification.name)

    class Meta:
        ordering = ['-device', '-created_at']
