from django.contrib import admin
from django.urls import path

from . import views
from . import mail_framework

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('mail/',mail_framework.send_mail, name='send_mail')
]
