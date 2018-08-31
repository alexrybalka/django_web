from django.contrib import admin
from .models import VehiclePart, Section


class AdminVehiclePart(admin.ModelAdmin):
    list_display = ('id', 'name', 'user', 'price', 'section')
    list_filter = ('section', 'user')
    list_editable = ('name', 'price', 'section')


class AdminSection(admin.ModelAdmin):
    list_display = ('id', 'name', 'user')
    list_filter = ('user', )


admin.site.register(VehiclePart, AdminVehiclePart)
admin.site.register(Section, AdminSection)
