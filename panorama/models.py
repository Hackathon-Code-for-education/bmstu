from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator



def user_directory_path(instance, filename):
    return 'users/user_{0}/{1}'.format(instance.user.id, filename)

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    text = models.CharField(max_length=200, null=False, blank=False)

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    text = models.CharField(max_length=600, null=False, blank=False)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(
        upload_to=user_directory_path,
        blank=True,
        null=True
    )
    birth_date = models.DateField(null=False, blank=False)
    phoneNumberRegex = RegexValidator(regex=r"^\+?1?\d{8,15}$")
    phoneNumber = models.CharField(validators=[phoneNumberRegex], max_length=16, unique=True, null=False, blank=False)
    education = models.CharField(max_length=600, blank=True,null=True)


class University(models.Model):
    admin_user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=False, blank=False)

    image = models.ImageField(
        upload_to=user_directory_path,
        blank=True,
        null=True
    )
    phoneNumberRegex = RegexValidator(regex=r"^\+?1?\d{8,15}$")
    phoneNumber = models.CharField(validators=[phoneNumberRegex], max_length=16, unique=True, null=False, blank=False)

    description = models.CharField(max_length=500, null=False, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)


