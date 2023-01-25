from django.db import models
from django.contrib.auth.models import User


class StudentAttandance(models.Model):
    student_name = models.name = models.ForeignKey(User, on_delete=models.CASCADE)
    student_roll = models.CharField(max_length=100)
    student_class = models.CharField(max_length=100)
    student_attandance = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def getAllStudentByDate(m,y):
        return StudentAttandance.objects.filter(updated_at__month=m,updated_at__year=y)
    