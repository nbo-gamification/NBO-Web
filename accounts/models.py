# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from onboarding.onboarding_constants import USER_PLAYER
from django.contrib.auth.models import (
    Group,
    UserManager,
    AbstractUser,
)
from django.core.validators import EmailValidator

# Create your models here.
class NBOUserManager(UserManager):
    use_in_migrations = True

    def create_user(self, email, password=None, **user_data):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            first_name=user_data['first_name'],
            last_name=user_data['last_name'],
            is_staff=False,
            is_superuser=False,
        )

        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **user_data):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=email,
            first_name=user_data['first_name'],
            last_name=user_data['last_name'],
            is_staff=True,
            is_superuser=True,
        )

        user.set_password(password)
        user.save()
        return user


class NBOUser(AbstractUser):
    email = models.EmailField('email address', unique=True, default='none@mail.com')
    username = models.CharField('username', max_length=1, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']
    validate_email = EmailValidator()
    username_validator = None

    objects = NBOUserManager()

    def __str__(self):
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        return self.first_name

    def rol_name(self):
        return ''
