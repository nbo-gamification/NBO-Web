from django.contrib import admin

from django.contrib.auth.admin import UserAdmin

from onboarding.models import (
    NBOUser,
)
# Register your models here.

admin.site.register(NBOUser, UserAdmin)
