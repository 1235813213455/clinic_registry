from django.contrib import admin
from django.contrib.admin import DateFieldListFilter

from .models import Doctor, Patient, Assignment


class AssignmentAdmin(admin.ModelAdmin):
    list_display = ('doctor', 'patient', 'date', 'time_string')
    list_filter = (('date', DateFieldListFilter), )
    search_fields = ('doctor__name', )

admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(Assignment, AssignmentAdmin)
