from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from Account.models import StudentAttendance
from django.contrib.auth.models import User
import datetime
from django.conf import settings
from django.utils.timezone import make_aware
from django.db.models import Count
from django.contrib import messages

naive_datetime = datetime.datetime.now()
naive_datetime.tzinfo

settings.TIME_ZONE
aware_datetime = make_aware(naive_datetime)
aware_datetime.tzinfo 

# Names = ['Beautiful Olinger', 'Maleyah Cothran', 'Mercedes Comer', 'Yanuel Foor', 'Dalia Munson', 'Justus Stribling', 'Ammy Garduno', 'Sicily Krantz', 'Austynn Turgeon', 'Loic Thiessen', 'Gryphon Stork', 'Sohum Hanke', 'Zariya Sandberg', 'Rishan Raphael', 'Marko Hardman', 'Aadi Sim', 'Ellis Diehl', 'Vail Natale', 'Kayana Villalba', 'Jayne Loftus', 'Ihsan Hovis', 'October Brockway', 'Hernan Howes', 'Shneur Meece', 'Zola Menard', 'Audric Schmucker', 'Jaziyah Nowicki', 'Taha Rohrer', 'Devion Graybill', 'Mayeli Geis', 'Boone Arevalo', 'Ryett Christner', 'Jayce Greene', 'Kolsen Rupe', 'Rivan Tennison', 'Jasmyn Snipes', 'Quinlan Stamm', 'Chris Cleveland', 'Everest Helman', 'Rylin Czarnecki', 'Kruz Christianson', 'Violett Godsey', 'Haven Tanner', 'Mahalia Gregor', 'Sholom Weinberger', 'Grettel Hock', 'Kaine South', 'Tariq Bergstrom', 'Rey Coe', 'Therese Baskin', 'Mariela Cyr', 'Helaina Madson', 'Karianna Bridwell', 'Jaykob Vital', 'Mendy Jacobi', 'Noemie Bono', 'Joslynn Lerma', 'Jovanni Banuelos', 'Dashiell Carrier', 'Allie Mckenzie', 'Moussa Ito', 'Makynlee Vicente', 'Terran Mitchum', 'Janel Nowakowski', 'Trenton Beard', 'Taleah Shinn', 'Randolph Etter', 'Makiyah Coyne', 'Rowyn Bloodworth', 'Armand Herd', 'Aariz Dionne', 'Maddy Mikesell', 'Jaia Brisson', 'Carma Frisbie', 'Karmello Lavergne', 'Kaitlynn Osorio', 'Lucianna Sisco', 'Kaison Thorpe', 'Ivie Towns', 'Khari Omeara', 'Edison Helton', 'Yisroel Hearn', 'Kristy Boring', 'Azaleah Farah', 'Mercer Hannigan', 'Andrew Hill', 'Akhil Rodas', 'Jamin Stanek', 'Maylin Brandenburg', 'Romel Scholz', 'Josefina Munguia', 'Cree Suzuki', 'Brithany Lazar', 'Deegan Harp', 'Gretel Mickey', 'Delphine Hatley', 'Maiya Cornwell', 'Kameren Files', 'Kobi Torrey', 'Tyson Christian', 'Aleeyah Staten', 'Karely Sessions', 'Arian Wroblewski', 'Sohan Goodale', 'Noreen Navarrette', 'Riggs Trainor', 'Aahan Vancamp', 'Azaria Blount', 'Sayuri Landa', 'Hillary Shanks', 'Ryden Canada', 'Letty Hammons', 'Treasure Fagan', 'Brantley Hershey', 'Lyric Chase', 'Brisa Vallejo', 'Taraji Hooks', 'Leobardo Dufresne', 'Anayah Brito', 'Chloe Peterson', 'Nyla Andrade', 'Aayush Mosier', 'Amorie Moretti', 'Lexie Gee', 'Carmyn Beaman', 'Dash Timmons', 'Austen Libby', 'Alyana Pedraza', 'Braylon Huynh', 'Eddison Tarin', 'Kallan Leonardo', 'Nami Dey', 'Melisa Tarr', 'Evyn Philip', 'Shayaan Bunton', 'Amaru Depasquale', 'Jenai Caffrey', 'Elie Delapena', 'Benjamin Moore', 'Aydrian Belisle', 'Adalind Frame', 'Maryana Reveles', 'Kaycen Cravens', 'Dashawn Mccallum', 'Johnnie Schiff', 'Shilah Peachey', 'Nori Vest', 'Lennon Goff', 'Aniyla Dinkins', 'Tysen Bodnar', 'Zayra Rude', 'Norberto Sealy', 'Imogen Dorman', 'Eugenia Korte', 'Samuel Allen', 'Ryder Boyd', 'Lillyan Denham', 'Chancellor Hutchings', 'Tayden Landrum', 'Tate Cisneros', 'Daysi Sill', 'Llewyn Desmarais', 'Easton Ellis', 'Asiyah Ballesteros', 'Scotlynn Backer', 'Haydee Trusty', 'Rain Peter', 'Chany Brotherton', 'Nadiyah Privett', 'Ishmael Hopson', 'Lamiya Alejo', 'Ben Miner', 'Jhene Almonte', 'Rajon Spiker', 'Yusuf Madison', 'Dixie Wiseman', 'Rosalina Hostetler', 'Yessica Sundberg', 'Harmony Francis', 'Santos Woodson', 'Yelena Kight', 'Subhan Harner', 'Favian Beecher', 'Darron Comfort', 'Sirius Rhyne', 'Xoe Binion', 'Cruze Shivers', 'Saint Cavender', 'Markeith Mathewson', 'Graison Hallam', 'Kashton Deluca', 'Ayush Falls', 'Mabel Connolly', 'Harmonie Holton', 'Dawsyn Laurence', 'Marelyn Kiss', 'Dalary Coyle', 'Braelynn Dudley', 'Katherin Burgin', 'Ayumi Brockett']

    
class HomeView(LoginRequiredMixin,View):
    login_url = 'login'
    redirect_field_name = 'login'
    def get(self, request):
        totalstudent = User.objects.all().exclude(is_superuser=True).count()
        student = StudentAttendance.getByMonth(2,2022)
        preset_students = student.filter(student_attandance=True).count()
        absebt_students = student.filter(student_attandance=False).count()
        
        total_record = preset_students + absebt_students
        start_date = student.order_by('created_at').first()
        last_date = student.order_by('created_at').last()
        
        result_list = student.filter(student_attandance=True).values('updated_at__day').annotate(dcount=Count('updated_at__day')).order_by()        
        count_list =[x['dcount'] for x in result_list]

        for i in range(len(student)):
            student[i]['created_at'] = student[i]['created_at'].strftime("%d-%m-%Y %H:%M:%S")
            student[i]['updated_at'] = student[i]['updated_at'].strftime("%d-%m-%Y %H:%M:%S")
            student[i]['student_attandance'] = "Present" if student[i]['student_attandance'] else "Absent"
            
        context = {
            "total":totalstudent,
            "present":preset_students,
            "absent":absebt_students,
            "total_record":total_record,
            "start":start_date,
            "last":last_date,
            "data" :[count_list,[i for i in range(1,30)],totalstudent],
            "month":list(student)
        }
        
        return render(request, 'Account/index.html',context)
    def post(self, request):
        student = StudentAttendance.getByMonth(2,2022)
        totalstudent = User.objects.all().exclude(is_superuser=True).count()
        print(request.POST.get("form_type"),"<<<<Form Type")
        if request.POST.get("form_type") == 'formAddStudent':
            username = request.POST.get('username')
            email = request.POST.get('email')
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            try:
                data = User.objects.create(username=username, email=email, first_name=first_name, last_name=last_name, password="12345678")
                data.save()
                messages.success(request, 'Student Added Successfully')
                totalstudent = User.objects.all().exclude(is_superuser=True).count()
            except:
                messages.error(request, 'Student Added Failed')
                
        elif request.POST.get("form_type") == 'formSearch':
            name = request.POST.get('name')
            date = request.POST.get('date')
            startdate = request.POST.get('date1')
            enddate = request.POST.get('date2')
            time = request.POST.get('time')
            subject = request.POST.get('standard')
            print(enddate,"<<<<Date")
            print(subject,"<<<<Subject")
            # try:
            student = StudentAttendance.searchData(name,date,startdate,enddate,time,subject)
            
            messages.success(request, 'Search Result Successfully')
            # except:
            #     print("Error.....")
            #     messages.error(request, 'Search Result Failed')
        
        elif request.POST.get("form_type") == 'formAttandance':
            pass
        
        preset_students = student.filter(student_attandance=True).count()
        absebt_students = student.filter(student_attandance=False).count()
        
        total_record = preset_students + absebt_students
        start_date = student.order_by('created_at').first()
        last_date = student.order_by('created_at').last()
        
        result_list = student.filter(student_attandance=True).values('updated_at__month').annotate(dcount=Count('updated_at__month')).order_by()        
        count_list =[x['dcount'] for x in result_list]
        
        for i in range(len(student)):
            student[i]['created_at'] = student[i]['created_at'].strftime("%d-%m-%Y %H:%M:%S")
            student[i]['updated_at'] = student[i]['updated_at'].strftime("%d-%m-%Y %H:%M:%S")
            student[i]['student_attandance'] = "Present" if student[i]['student_attandance'] else "Absent"
            
        context = {
            "total":totalstudent,
            "present":preset_students,
            "absent":absebt_students,
            "total_record":total_record,
            "start":start_date,
            "last":last_date,
            "data" :[count_list,[i for i in range(1,12)],30],
            "month":list(student)
        }
        
        return render(request, 'Account/index.html',context)
    
class LoginView(View,LoginRequiredMixin, UserPassesTestMixin):
    def get(self, request):
        
        # Base method with no type specified
       
        # for i in range(1,12):
        #     for j in range(1,28):
        #         for name in Names:
        #             student_roll = "202200"+str(Names.index(name))
        #             student_name = name
        #             first_name = name.split()[0]
        #             last_name = name.split()[1]
        #             student_attandance = bool(random.getrandbits(1))
        #             student_class = "MCA"
        #             # 2023-01-22 21:35:23.115037
        #             created_at = datetime.datetime(2022, i, j, 10, random.randint(1, 59), random.randint(1, 59),000000, tzinfo=pytz.UTC)
        #             updated_at = created_at
        #             # date_joined = datetime.date(2022,1,1)
        #             # user = User.objects.create(username=first_name+last_name, email=first_name+"@gmail.com", first_name=first_name, last_name=last_name, password="12345678", date_joined=date_joined)
        #             # user.save()
        #             # print(user)
        #             data = StudentAttandance(student_name=User.objects.get(username=first_name+last_name),student_roll=student_roll,student_class=student_class,student_attandance=student_attandance,created_at=created_at,updated_at=updated_at)
        #             print(data)
        #             data.save()
        if request.user.is_authenticated:
            return redirect('home')
        return render(request, 'Account/login.html')
    
    def test_func(self):
        print(self.request.user.is_superuser,"<< super user")
        print(self.request.user.username,"<< user name")
        return self.request.user.is_superuser or self.request.user.is_staff
    
    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        self.test_func()
        if user is not None:
            login(request, user)
            print('User is logged in')
            return redirect('home')
        else:
            print('User is not logged in')
            return render(request, 'Account/login.html')
    
class ForgotPasswordView(View):
    def get(self, request):
        return render(request, 'Account/forgot-password.html')
    def post(self, request):
        return render(request, 'Account/forgot-password.html')
    
class Error404View(View):
    def get(self, request):
        return render(request, 'Account/404.html')
    def post(self, request):
        return render(request, 'Account/404.html')
    
class Error500View(View):
    def get(self, request):
        return render(request, 'Account/500.html')
    def post(self, request):
        return render(request, 'Account/500.html')

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login')
