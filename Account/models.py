from django.db import models
from django.contrib.auth.models import User


class StudentAttendance(models.Model):
    student_id = models.name = models.ForeignKey(User, on_delete=models.CASCADE)
    student_roll = models.CharField(max_length=100)
    student_class = models.CharField(max_length=100)
    student_attandance = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def getByMonth(month,year):
        return StudentAttendance.objects.filter(updated_at__month=month,updated_at__year=year).values('student_id','student_id__username','student_roll','student_class','student_attandance','updated_at','created_at')
    
    def searchData(name,date,startdate,enddate,time,subject):
        if name == '' and date == '' and time == '' and subject == '' and startdate == '' and enddate == '':
            return StudentAttendance.objects.values('student_id','student_id__username','student_roll','student_class','student_attandance','updated_at','created_at')
        else:
            return StudentAttendance.objects.values('student_id','student_id__username','student_roll','student_class','student_attandance','updated_at','created_at').filter(student_id__username__icontains=name,updated_at__gte=startdate,updated_at__lte=enddate)
            
    