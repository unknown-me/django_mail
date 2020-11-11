from django.urls import path
from django.conf.urls import url

from mail.api.views import SendMyMail

app_name = 'mail-api'

urlpatterns = [
    path('send_mail', SendMyMail.as_view(), name="send_mail"),
]