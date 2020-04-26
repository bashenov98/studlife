from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, UserManager
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.utils.translation import gettext_lazy as _
from django.core.mail import send_mail

from utils.constants import FACULTIES, FIT, ISE
from utils.validators import extension_validator, file_size_validator


class AbstractUser(AbstractBaseUser, PermissionsMixin):
    username_validator = UnicodeUsernameValidator()

    username = models.CharField(
        _('username'),
        max_length=30,
        unique=True,
        validators=[username_validator],
        error_messages={
            'unique': _("This username is already taken"),
            'max_length': _("Too many characters"),
        }
    )

    objects = UserManager()

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        abstract = True


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(
        _('first_name'),
        max_length=30,
        blank=True
    )
    last_name = models.CharField(
        _('last_name'),
        max_length=30,
        blank=True
    )
    is_staff = models.BooleanField(
        _('staff status'),
        default=False
    )
    is_student = models.BooleanField(
        _('student status'),
        default=False
    )
    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return f'{self.id}: {self.username}'


class Organization(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(default="")
    image = models.ImageField(upload_to='media/images',
                              validators=[extension_validator,
                                          file_size_validator],
                              null=True, blank=True)
    president = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.username


class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='media/images',
                              validators=[extension_validator,
                                          file_size_validator],
                              null=True, blank=True)
    bio = models.TextField(max_length=500)
    faculty = models.PositiveSmallIntegerField(choices=FACULTIES, default=FIT)
    organization = models.ForeignKey(Organization, on_delete=models.DO_NOTHING)





