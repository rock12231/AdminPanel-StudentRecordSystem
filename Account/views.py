from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from Account.models import StudentAttandance
from django.contrib.auth.models import User
import random
import datetime
import pytz
from django.utils import timezone
from django.conf import settings
from django.utils.timezone import make_aware

naive_datetime = datetime.datetime.now()
naive_datetime.tzinfo

settings.TIME_ZONE
aware_datetime = make_aware(naive_datetime)
aware_datetime.tzinfo 

Names = ['Beautiful Olinger', 'Maleyah Cothran', 'Mercedes Comer', 'Yanuel Foor', 'Dalia Munson', 'Justus Stribling', 'Ammy Garduno', 'Sicily Krantz', 'Austynn Turgeon', 'Loic Thiessen', 'Gryphon Stork', 'Sohum Hanke', 'Zariya Sandberg', 'Rishan Raphael', 'Marko Hardman', 'Aadi Sim', 'Ellis Diehl', 'Vail Natale', 'Kayana Villalba', 'Jayne Loftus', 'Ihsan Hovis', 'October Brockway', 'Hernan Howes', 'Shneur Meece', 'Zola Menard', 'Audric Schmucker', 'Jaziyah Nowicki', 'Taha Rohrer', 'Devion Graybill', 'Mayeli Geis', 'Boone Arevalo', 'Ryett Christner', 'Jayce Greene', 'Kolsen Rupe', 'Rivan Tennison', 'Jasmyn Snipes', 'Quinlan Stamm', 'Chris Cleveland', 'Everest Helman', 'Rylin Czarnecki', 'Kruz Christianson', 'Violett Godsey', 'Haven Tanner', 'Mahalia Gregor', 'Sholom Weinberger', 'Grettel Hock', 'Kaine South', 'Tariq Bergstrom', 'Rey Coe', 'Therese Baskin', 'Mariela Cyr', 'Helaina Madson', 'Karianna Bridwell', 'Jaykob Vital', 'Mendy Jacobi', 'Noemie Bono', 'Joslynn Lerma', 'Jovanni Banuelos', 'Dashiell Carrier', 'Allie Mckenzie', 'Moussa Ito', 'Makynlee Vicente', 'Terran Mitchum', 'Janel Nowakowski', 'Trenton Beard', 'Taleah Shinn', 'Randolph Etter', 'Makiyah Coyne', 'Rowyn Bloodworth', 'Armand Herd', 'Aariz Dionne', 'Maddy Mikesell', 'Jaia Brisson', 'Carma Frisbie', 'Karmello Lavergne', 'Kaitlynn Osorio', 'Lucianna Sisco', 'Kaison Thorpe', 'Ivie Towns', 'Khari Omeara', 'Edison Helton', 'Yisroel Hearn', 'Kristy Boring', 'Azaleah Farah', 'Mercer Hannigan', 'Andrew Hill', 'Akhil Rodas', 'Jamin Stanek', 'Maylin Brandenburg', 'Romel Scholz', 'Josefina Munguia', 'Cree Suzuki', 'Brithany Lazar', 'Deegan Harp', 'Gretel Mickey', 'Delphine Hatley', 'Maiya Cornwell', 'Kameren Files', 'Kobi Torrey', 'Tyson Christian', 'Aleeyah Staten', 'Karely Sessions', 'Arian Wroblewski', 'Sohan Goodale', 'Noreen Navarrette', 'Riggs Trainor', 'Aahan Vancamp', 'Azaria Blount', 'Sayuri Landa', 'Hillary Shanks', 'Ryden Canada', 'Letty Hammons', 'Treasure Fagan', 'Brantley Hershey', 'Lyric Chase', 'Brisa Vallejo', 'Taraji Hooks', 'Leobardo Dufresne', 'Anayah Brito', 'Chloe Peterson', 'Nyla Andrade', 'Aayush Mosier', 'Amorie Moretti', 'Lexie Gee', 'Carmyn Beaman', 'Dash Timmons', 'Austen Libby', 'Alyana Pedraza', 'Braylon Huynh', 'Eddison Tarin', 'Kallan Leonardo', 'Nami Dey', 'Melisa Tarr', 'Evyn Philip', 'Shayaan Bunton', 'Amaru Depasquale', 'Jenai Caffrey', 'Elie Delapena', 'Benjamin Moore', 'Aydrian Belisle', 'Adalind Frame', 'Maryana Reveles', 'Kaycen Cravens', 'Dashawn Mccallum', 'Johnnie Schiff', 'Shilah Peachey', 'Nori Vest', 'Lennon Goff', 'Aniyla Dinkins', 'Tysen Bodnar', 'Zayra Rude', 'Norberto Sealy', 'Imogen Dorman', 'Eugenia Korte', 'Samuel Allen', 'Ryder Boyd', 'Lillyan Denham', 'Chancellor Hutchings', 'Tayden Landrum', 'Tate Cisneros', 'Daysi Sill', 'Llewyn Desmarais', 'Easton Ellis', 'Asiyah Ballesteros', 'Scotlynn Backer', 'Haydee Trusty', 'Rain Peter', 'Chany Brotherton', 'Nadiyah Privett', 'Ishmael Hopson', 'Lamiya Alejo', 'Ben Miner', 'Jhene Almonte', 'Rajon Spiker', 'Yusuf Madison', 'Dixie Wiseman', 'Rosalina Hostetler', 'Yessica Sundberg', 'Harmony Francis', 'Santos Woodson', 'Yelena Kight', 'Subhan Harner', 'Favian Beecher', 'Darron Comfort', 'Sirius Rhyne', 'Xoe Binion', 'Cruze Shivers', 'Saint Cavender', 'Markeith Mathewson', 'Graison Hallam', 'Kashton Deluca', 'Ayush Falls', 'Mabel Connolly', 'Harmonie Holton', 'Dawsyn Laurence', 'Marelyn Kiss', 'Dalary Coyle', 'Braelynn Dudley', 'Katherin Burgin', 'Ayumi Brockett']

    
class HomeView(LoginRequiredMixin,View):
    login_url = 'login'
    redirect_field_name = 'login'
    def get(self, request):
        totalstudent = User.objects.all().exclude(is_superuser=True).count()
        preset_students = StudentAttandance.objects.filter(student_attandance=True).count()
        absebt_students = StudentAttandance.objects.filter(student_attandance=False).count()
        total_record = preset_students + absebt_students
        start_date = StudentAttandance.objects.all().order_by('created_at').first().created_at
        last_date = StudentAttandance.objects.all().order_by('created_at').last().created_at
        listdata = []
        for i in range(1,30):
            OneDayPresentStudent = StudentAttandance.objects.filter(updated_at__month=1,updated_at__day=i,updated_at__year=2022,student_attandance=False).count()
            listdata.append(OneDayPresentStudent)
        # print(listdata,"<<<<< List Data")
        # print(OneDayPresentStudent,"<<<<< One DAY")
        # list_of_absent_day_by_day  StudentAttandance.objects.filter(created_at__day=1).count()
        # jan = StudentAttandance.objects.filter(created_at__day=1).count()
        # print(jan,"<<<<< Count of jan")
        #One month student data fetch
        OneMonthStudent = StudentAttandance.objects.filter(updated_at__month=1,updated_at__year=2022).values()
        # OneMonthStudent attendance false to 0 and true to 1 date to string
        for i in OneMonthStudent:
            if i['student_attandance'] == False:
                i['student_attandance'] = 0
            else:
                i['student_attandance'] = 1
            i['updated_at'] = i['updated_at'].strftime("%d-%m-%Y")
            i['created_at'] = i['created_at'].strftime("%d-%m-%Y")
        
        print(OneMonthStudent,"<<<<< One Month")
        context = {
            "total":totalstudent,
            "present":preset_students,
            "absent":absebt_students,
            "total_record":total_record,
            "start":start_date,
            "last":last_date,
            "data" :[listdata,[i for i in range(1,30)]],
            #"month":list(OneMonthStudent)
        }
        return render(request, 'Account/index.html',context)
    def post(self, request):
        return render(request, 'Account/index.html')
    
class LoginView(View,LoginRequiredMixin, UserPassesTestMixin):
    def get(self, request):
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
        print(username, password)
        user = authenticate(request, username=username, password=password)
        self.test_func()
        print(self.test_func(),"<<< Function")
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
