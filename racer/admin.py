from django.contrib import admin
from .models import Racer, Zavod

class RacerAdmin(admin.ModelAdmin):
  list_display = ("firstname", "lastname", "sex", "date", "email", "phone")
  
admin.site.register(Racer, RacerAdmin)

class ZavodAdmin(admin.ModelAdmin):
  list_display = ("name", "date", "info")
  
admin.site.register(Zavod, ZavodAdmin)