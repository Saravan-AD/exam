from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('signup',views.signup,name='signup'),
    path('signinfac',views.signinfac,name='signinfac'),
    path('signout',views.signout,name='signout'),
    path('updatecontent',views.update_content,name='updatecontent'),
    path('dashboard/',views.dashboard,name='dashboard')
]
