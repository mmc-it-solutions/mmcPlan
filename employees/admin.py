from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Employee
# Register your models here.


@admin.register(Employee)
class EmployeeAdmin(UserAdmin):
    pass
