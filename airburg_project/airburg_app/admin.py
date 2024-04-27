from django.contrib import admin
from .models import *


class CapitanAdmin(admin.ModelAdmin):
    list_display = ('name', "surname", "experience")
    list_filter = ('experience', "surname")


class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', "country")
    list_filter = ('name', "country")


class AirplaneAdmin(admin.ModelAdmin):
    list_display = ('name', "wight", "count_pass", "fuel_reserve", "company", "capitan")
    list_filter = ('wight', "count_pass", "company")


admin.site.register(Capitan, CapitanAdmin)
admin.site.register(Airplane, AirplaneAdmin)
admin.site.register(Company, CompanyAdmin)
