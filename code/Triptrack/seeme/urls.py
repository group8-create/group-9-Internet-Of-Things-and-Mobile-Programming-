from django.urls import path
from seeme import views

urlpatterns = [
    path('', views.home, name='home'),
    path('driver/', views.driver, name='driver'),
    path('map/', views.map, name='map'),
    path('signup/', views.usersignup, name='usersignup'),
    path('driversignup/ <str:pk>/', views.driverregistration, name='driversignup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('save_location/', views.save_location, name='save_location'),

    path('mapping/ <str:pk>/ ', views.mapping, name='mapping'),
    path('usersetting/<str:pk>/ ', views.usersetting, name='usersetting'),
    path('drivermap/ ', views.drivermap, name='drivermap'),
    path('my-django-view/<str:pk>/', views.my_django_view, name='my_django_view'),


]