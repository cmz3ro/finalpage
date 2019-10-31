"""copysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from main_app.views import main_app1,net_gh,treni,rapid,tumba,commanda,vorota,sopernik,produkiay,sbori1
from about.views import new1,contacts,add_contact
from django.conf.urls import url, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_app1),
    path('about/', new1),
    path('contacts/',contacts),
    path('new/', net_gh),
    path('treni/',treni),
    path('sbori/',rapid),
    path('sbori1/',sbori1),
    path('tumba/',tumba),
    path('commanda/',commanda),
    path('vorota/',vorota),
    path('sopernik/',sopernik),
    path('produkiay/',produkiay),
    path('contacts/add_message/',add_contact),
]
