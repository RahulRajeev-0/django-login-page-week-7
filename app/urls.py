
from django.urls import path,include
from app import views

urlpatterns = [

    path('',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('login/',views.handlelogin,name='handlelogin'),
    path('logout/',views.handlelogout,name='handlelogout'),
    path('signup',views.handlesignup,name='handlesignup'),
    
]