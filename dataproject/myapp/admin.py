from django.contrib import admin
from .models import Student,StudentAdmin,Employee,EmployeeAdmin


admin.site.register(Student,StudentAdmin)
admin.site.register(Employee,EmployeeAdmin)
