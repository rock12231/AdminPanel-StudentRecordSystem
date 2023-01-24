from django.contrib import admin
from django.urls import path
from Account.views import HomeView, LoginView, ForgotPasswordView, Error404View, Error500View, LogoutView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('login/', LoginView.as_view(), name='login'),
    path('forgot-password/', ForgotPasswordView.as_view(), name='forgot-password'),
    path('error-404/', Error404View.as_view(), name='error-404'),
    path('error-500/', Error500View.as_view(), name='error-500'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
