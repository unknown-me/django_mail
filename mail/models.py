from django import forms
from django.db import models


# Create your models here.

class MyMailConfig(models.Model):
    email_id = models.EmailField()
    email_password = models.CharField(max_length=32)


class MyMailContent(models.Model):
    mail_to = models.EmailField()
    mail_content = models.CharField(max_length=3000)
    mail_subject = models.CharField(max_length=1000)
    mail_attachment = models.FileField(blank=True, upload_to='attachment/')

    def __str__(self):
        return self.mail_to