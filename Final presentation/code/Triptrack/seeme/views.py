from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import *
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.

USERLOGIN = 0
USERNAME = ''
def home(request):
    # user = User.objects.first()
    # context = {
    #     'user': user
    # }
    return render(request, 'seeme/home.html',{'test':USERLOGIN})

def driver(request):
    return render(request, 'seeme/driver.html',{'test':USERLOGIN} )


@login_required(login_url='signup')
def map(request, pk):
    if USERLOGIN == 1:
        pk = User.use_id
        return render(request, 'seeme/map.html', {'test':USERLOGIN,'pk':pk})
    else:
        return render(request, 'seeme/home.html')
    
# TODO:  USER SIGN UP

def usersignup(request):
    global USERLOGIN
    if request.method == 'POST':
        username=request.POST.get('username')
        username = username.lower()
        email=request.POST.get('email')
        password=request.POST.get('password')
        
        usernames = User.objects.all()

        for i in usernames:
            if username == i.username:

                print(i.username)
                return render(request, 'seeme/home.html', {'error_message': 'Username already exists'})
        else:
            userform = User.objects.create(
                username = username,
                email = email,
                password = password,
            )
            userform.save()
            print('user created')
            USERLOGIN = 1
            pk=userform.use_id
                    
            return render(request, 'seeme/map.html',{'pk':pk,'test':USERLOGIN})
    
    return render('seeme/home.html',{'pk':pk,'test':USERLOGIN})

#TODO: USER LOGIN

def login(request):
    global USERLOGIN,USERNAME
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            user = None
        try:
            driver_login = Driver.objects.get(dri_user=user)
        except Driver.DoesNotExist:
            driver_login = None

        print(driver_login) 
        try:  
            if driver_login is not None and user.password == password:
                print('driver login succesful')
                USERLOGIN = 1
                pk=driver_login.dri_id
                print(pk)
                return redirect('drivermap')
                return render(request,'seeme/map_driver.html',{'pk':pk,'test':USERLOGIN})
        except:
            print('driver doesnot exists')
        if user is not None and user.password == password:
            print('login succesful')
            USERLOGIN = 1
            pk=user.use_id
            USERNAME = user
            messages.success(request, 'login succesful')

            return render(request,'seeme/map.html',{'pk':pk,'test':USERLOGIN})
        
        else:
            # Return an 'invalid login' error message.
            print('invalid login')  
            USERLOGIN = 0
            messages.error(request, 'incorrect username or password')

            return render(request, 'seeme/home.html', {'error_message': 'Invalid login'})
    return render(request, 'seeme/home.html', {'test':USERLOGIN})
    
# TODO: DRIVER REGISTRATION

def driverregistration(request,pk):
    global USERLOGIN
    
    mainuser = User.objects.get(use_id=pk)
    if request.method == 'POST':
        fullname = request.POST.get('fullname')
        license = request.POST.get('license')
        image = request.FILES.get('image')
        # try:
        #     driver = Driver.objects.get(dri_user=User.use_id)        
        # except driver.DoesNotExist:
        #     driver = None
        user = Driver.objects.create(
            fullname=fullname, 
            license=license,
            image=image,
            dri_user = mainuser,
        )
        USERLOGIN = 1
        
        user.save()
        return redirect('drivermap')
    
    return render(request, 'seeme/driver.html',{'test':USERLOGIN,'pk':pk})

# TODO: LOGOUT FUNCTIONALITY
def logout(request):
    global USERLOGIN,USERNAME
    USERLOGIN = 0
    pk = User.objects.get(username = USERNAME)
    try:
        user_delete = Passenger.objects.get(pas_user=pk.use_id)
        user_delete.delete()
        user_destination = Destination.objects.get(passenger=pk.use_id)
        user_destination.delete()
    except Passenger.DoesNotExist:
        print('no data')
    messages.success(request, 'logged out sueccesful')
    return redirect('home')   




def save_location():
        pass



def mapping(request, pk):
    if USERLOGIN == 1:
        pk = User.use_id
        return render(request, 'seeme/map.html', {'test':USERLOGIN,'pk':pk})
    else:
        return render(request, 'seeme/home.html')
    
def usersetting(request, pk):
    global USERLOGIN
    USERLOGIN = 1
    return render(request, 'seeme/setting.html', {'pk':pk,'test':USERLOGIN})

def drivermap(request):
    global USERLOGIN
    passengers = Passenger.objects.all()
    destination = Destination.objects.all()
    context = []
    USERLOGIN = 1
    for i in passengers:
        for j in destination:
            if i.pas_user.use_id == j.passenger.use_id:
                context.append({
                    'lat':i.current_loc_lat,
                    'lng':i.current_loc_lng,
                    'des':j.des_name})
    passenger_data = json.dumps(context)
    print(passenger_data)
    return render(request, 'seeme/map_driver.html',{'test':USERLOGIN,'datapassenger':passenger_data} )
@csrf_exempt
def my_django_view(request,pk):
    global USERLOGIN,USERNAME
    USERLOGIN = 1
    get_id = User.objects.get(username = USERNAME)
    print(get_id)
    if request.method == 'POST':
        data = json.loads(request.body)
        destination_name = data['destination_name']
        latitude = data['latitude']
        longitude = data['longitude']
        
        # Save the data to your database
        print(destination_name,'\n')
        print(latitude,longitude)

        # Loop through the destinations and get the passengers for each destination
        
        # check if the destination already exists
        try:
            destinations = Destination.objects.all()
            for i in destinations:            
                if get_id == i.passenger:
                    i.delete()
        except:
            print('test')
        # we store user details by latitude and longitude

        try:
            locations = Passenger.objects.all()
            for i in locations:            
                if get_id == i.passenger:
                    i.delete()
        except:
            print('test passenger location')
        
        # storing user destination
         
        location = Passenger.objects.update_or_create(
                current_loc_lat = latitude,
                current_loc_lng = longitude,
                pas_user = USERNAME,


        )

        destination = Destination.objects.update_or_create(
            des_name = destination_name, 
            passenger = get_id,
        )
        print('successfully stored')

        return render(request, 'seeme/map.html', {'test':USERLOGIN,'pk':get_id})
    return render(request, 'seeme/map.html', {'test':USERLOGIN,'pk':get_id})
