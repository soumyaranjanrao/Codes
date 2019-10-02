from django.contrib import admin
from empdetails.models import Employee

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name','emp_id']

# Register your models here.
admin.site.register(Employee,EmployeeAdmin)
