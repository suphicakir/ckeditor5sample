from django.contrib import admin
from . import models as m

# Register your models here.
@admin.register(m.MyTestApp)
class AdminMyTestApp (admin.ModelAdmin):
    list_display=('title',)