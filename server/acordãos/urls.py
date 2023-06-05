"""
URL configuration for acordãos project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path,include,re_path
from drf_social_oauth2 import urls
from rest_framework_swagger.views import get_swagger_view
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.views.static import serve
from rest_framework import permissions
from django.conf import settings
schema_view = get_schema_view(
    openapi.Info(
        title="acordãos",
        default_version="v1",
        description="Documentation for the acordãos API",
        contact=openapi.Contact(email="lumafepe@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)



urlpatterns = [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path("admin/", admin.site.urls),
    
    path('api-auth/', include('rest_framework.urls')),
    path('api-auth/', include('drf_social_oauth2.urls',namespace='drf')),
    path('accounts/', include('accounts.urls',namespace="accounts")),
    path('favorites/', include('favorites.urls',namespace="favorites")),
    path('records/', include('records.urls',namespace="records")),
    re_path(r"^static/(?P<path>.*)$", serve, {"document_root": settings.STATIC_ROOT}),
]
