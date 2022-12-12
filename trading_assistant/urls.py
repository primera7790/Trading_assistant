"""trading_assistant URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf.urls.static import static
from django.conf import settings

from main_interface.views import index, init_base, init_current, init_auto_mode, init_disable_auto_mode, change_settings, show_balance

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('init_base/', init_base, name='init_base'),
    path('init_current/', init_current, name='init_current'),
    path('init_auto_mode/', init_auto_mode, name='init_auto_mode'),
    path('init_disable_auto_mode/', init_disable_auto_mode, name='init_disable_auto_mode'),
    path('settings/', change_settings, name='settings_page'),
    path('balance/', show_balance, name='balance'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)