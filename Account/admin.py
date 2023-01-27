from django.contrib import admin
from Account.models import StudentAttendance
# Register your models here.

class StudentAttendanceTable(admin.ModelAdmin):
    list_display = ['student_id','student_roll','student_class','student_attandance','created_at','updated_at']
admin.site.register(StudentAttendance,StudentAttendanceTable)