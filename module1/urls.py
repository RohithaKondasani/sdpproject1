from django.contrib import admin
from django.urls import path
from .views import*


urlpatterns = [
    path('hello1/',hello1, name='hello'),
    path('',newhomepage, name='newhomepage'),
    path('package/',travelpackage,name = 'package'),
    path('print/',print_to_console, name= 'print_to_console'),
    path('p/',print1,name='print'),
    path('randomcall/',randomcall, name= 'randomcall'),
    path('randomlogic/', randomlogic, name='randomlogic'),
    path('date/',getdate1,name='getdate1'),
    path('date1/',get_date,name='get_date'),
    path('registercall/',registercall,name='register_call'),
    path('registerloginfunction/',registerloginfunction,name = 'registerloginfunction'),
    path('pie/',pie_chart,name='pie_chart'),
    path('car/',rentcar,name='rent_car'),
    path('weathercall/',weatherpagecall,name= 'weatherpagecall'),
    path('weatherlogic/',weatherlogic,name= 'weatherlogic'),
    path('feedbackcall/', feedback_call, name='feedback_call'),
    path('contactmail/', contactmail, name='contactmail'),
    path('login/',login,name='login'),
    path('signup/',signup,name='signup'),
    path('login1/',login1,name='login1'),
    path('signup1/',signup1,name='signup1'),
    path('logout/',logout,name='logout'),

]