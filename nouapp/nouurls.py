from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('',views.index,name='index'),
    path('aboutus/',views.aboutus,name='aboutus'),
    path('aboutam/',views.about2,name='about2'),
    path('aboutas/',views.about3,name='about3'),
    path('abouthb/',views.about4,name='about4'),
    path('aboutr/',views.about5,name='about5'),
    path('login/',views.login,name='login'),
    path('registration/',views.registration,name='registration'),
    path('contactus/',views.contactus,name="contactus"),
    path('forgotpass/',views.forgotpass,name="forgotpass"),
    
    
]
