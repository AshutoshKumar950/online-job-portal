from django.contrib import admin
from django.urls import path

from mainapp import views
from adminapp.views import *
from userapp.views import *

urlpatterns = [

    # ==========================
    # Django Admin
    # ==========================
    path('admin/', admin.site.urls),

    # ==========================
    # Main Pages
    # ==========================
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),

    # ==========================
    # Jobs
    # ==========================
    path('jobs/', viewjobs, name='jobs'),
    path('viewjobs/', viewjobs, name='viewjobs'),

    # ==========================
    # Admin
    # ==========================
    path('admindash/', admindash, name='admindash'),
    path('adminlogout/', adminlogout, name='adminlogout'),

    path('jobseeker/', jobseeker, name='jobseeker'),

    path('postjob/', postjob, name='postjob'),

    path('postedjob/', postedjob, name='postedjob'),

    # path('deletejob/<int:id>/', deletejob, name='deletejob'),

    path('enquiries/', enquiries, name='enquiries'),

    path('deleteenq/<int:id>/', deleteenq, name='deleteenq'),

    path('changeadminpwd/', changeadminpwd, name='changeadminpwd'),

    path('viewfeedback/', viewfeedback, name='viewfeedback'),

    path('viewcomplaint/', viewcomplaint, name='viewcomplaint'),

    # ==========================
    # User
    # ==========================
    path('userdash/', userdash, name='userdash'),

    path('viewjobs/', viewjobs, name='viewjobs'),

    path('viewprofile/', viewprofile, name='viewprofile'),

    path('viewresponse/', viewresponse, name='viewresponse'),

    path('giveresponse/', giveresponse, name='giveresponse'),

    path('changeuserpwd/', changeuserpwd, name='changeuserpwd'),

    path('userlogout/', userlogout, name='userlogout'),

]