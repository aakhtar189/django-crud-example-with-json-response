from django.contrib import admin

from .models import Student

class StudentAdmin(admin.ModelAdmin):
    list_display = ['user', 'nationality']
    search_fields = ['user__first_name', 'user__last_name']

admin.site.register(Student, StudentAdmin)
