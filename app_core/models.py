from django.db import models
from django_ckeditor_5.fields import CKEditor5Field


# Create your models here.
class MyTestApp (models.Model):
    title=models.CharField(max_length=250)
    body=CKEditor5Field('Text', config_name='extends')