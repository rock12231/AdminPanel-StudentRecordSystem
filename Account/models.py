from django.db import models
from django.contrib.auth.models import User
import datetime


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
            if date :
                Cdate = date.split('-')
                cDay = int(Cdate[2])
                cMonth = int(Cdate[1])	
                cYear = int(Cdate[0])
            if startdate :
                Sdate = startdate.split('-')
                sDay= int(Sdate[2])
                sMonth = int(Sdate[1])
                sYear = int(Sdate[0])
            if enddate :
                Edate = enddate.split('-')
                eDay= int(Edate[2])
                eMonth = int(Edate[1])
                eYear = int(Edate[0])
                print(sDay,sMonth,sYear,"==date==",eDay,eMonth,eYear)
            return StudentAttendance.objects.values('student_id','student_id__username','student_roll','student_class','student_attandance','updated_at','created_at').filter(student_id__username__icontains=name,updated_at__date__range=(datetime.date(sYear,sMonth,sDay), datetime.date(eYear,eMonth,eDay)))