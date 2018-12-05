from django.contrib import admin

from django.contrib.auth.admin import UserAdmin

from onboarding.models import (
    Activity,
    ActivityType,
    Briteling,
    Category,
    CategoryOffice,
    CategoryOfficeActivity,
    ConnectActivity,
    Office,
    PlayerOfficeProgress,
    PlayerCategoryOfficeProgress,
    NBOUser,
)
# Register your models here.

admin.site.register(NBOUser, UserAdmin)
admin.site.register(Office)
admin.site.register(Category)
admin.site.register(ActivityType)
admin.site.register(Activity)
admin.site.register(CategoryOffice)
admin.site.register(CategoryOfficeActivity)
admin.site.register(PlayerCategoryOfficeProgress)
admin.site.register(PlayerOfficeProgress)
admin.site.register(ConnectActivity)
admin.site.register(Briteling)
