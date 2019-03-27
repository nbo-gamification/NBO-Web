from django.contrib import admin
from polymorphic.admin import (
    PolymorphicParentModelAdmin,
    PolymorphicChildModelAdmin,
)
from .models import (
    Activity,
    ConnectActivity,
)


@admin.register(ConnectActivity)
class ModelConnectAdmin(PolymorphicChildModelAdmin):
    base_model = ConnectActivity


@admin.register(Activity)
class ModelActivityAdmin(PolymorphicParentModelAdmin):
    """ The parent model admin """
    child_models = (ModelConnectAdmin, )
