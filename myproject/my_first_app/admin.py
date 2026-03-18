from django.contrib import admin

# Register your models here.
from .models import Employee

# admin.site.register(Employee)
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'empname', 'phone', 'email', 'date')
