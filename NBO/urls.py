"""NBO URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from onboarding.urls import rest_urls
from rest_framework import permissions
from accounts.rest_views import CustomLoginView


schema_view = get_schema_view(
    openapi.Info(
        title="NBO API",
        default_version='v1',
        description="NBO API information",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    url(r'^api/schema$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('admin/', admin.site.urls),
    url(r'api/', include(rest_urls)),
    url(r'rest-auth/login', CustomLoginView.as_view(), name='custom_login'),
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^accounts/', include('accounts.urls')),
    url(r'', include('onboarding.urls')),
]
