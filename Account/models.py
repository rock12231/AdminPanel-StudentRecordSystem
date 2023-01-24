from django.db import models
from django.contrib.auth.models import User


class StudentAttandance(models.Model):
    student_name = models.name = models.ForeignKey(User, on_delete=models.CASCADE)
    student_roll = models.CharField(max_length=100)
    student_class = models.CharField(max_length=100)
    student_attandance = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
             
    # def __init__() -> None:
    #     student_name = randstr()
        
    # date=datetime.date(randint(2005,2025), randint(1,12),randint(1,28))
    # print
# d1 = datetime.strptime('1/1/2008 1:30 PM', '%m/%d/%Y %I:%M %p')
# d2 = datetime.strptime('1/1/2009 4:50 AM', '%m/%d/%Y %I:%M %p')

# print(random_date(d1, d2))