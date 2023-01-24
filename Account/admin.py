from django.contrib import admin
from Account.models import StudentAttandance
# Register your models here.

class StudentAttandanceTable(admin.ModelAdmin):
    list_display = ['student_name','student_roll','student_class','student_attandance','created_at','updated_at']
admin.site.register(StudentAttandance,StudentAttandanceTable)