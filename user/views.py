from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import HotelBooking, User
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponseRedirect, JsonResponse
from django.contrib.auth import authenticate,login
from.models import (Amenities,Hotel)
from django.db.models import Q
# Create your views here.
def user(request):
    return render(request,'user')
# def base(request):
#     return render(request,'base.html')

def check_booking(start_date  , end_date ,uid , room_count):
    qs = HotelBooking.objects.filter(
        start_date__lte=start_date,
        end_date__gte=end_date,
        hotel__uid = uid
        )
    
    if len(qs) >= room_count:
        return False
    
    return True

def homepage(request):
    amenities_objs = Amenities.objects.all()
    hotels_objs = Hotel.objects.all()
    

    sort_by = request.GET.get('sort_by')
    search = request.GET.get('search')
    amenities = request.GET.getlist('amenities')
    print(amenities)

    if sort_by:
        
        if sort_by == 'ASC':
            hotels_objs = hotels_objs.order_by('hotel_price')
        elif sort_by == 'DSC':
            hotels_objs = hotels_objs.order_by('-hotel_price')  


    
    if search:
        hotels_objs = hotels_objs.filter(
            Q(hotel_name__icontains = search) |
            Q(description__icontains = search) )

    if len(amenities):
        hotels_objs=hotels_objs.filter(amenities__amenity_name__in = amenities).distinct()

    
    
    context = {'amenities_objs' : amenities_objs , 'hotels_objs' : hotels_objs , 'sort_by' : sort_by 
    , 'search' : search,'amenities':amenities }
    return render(request,'homepage.html',context)

def hotel_detail(request,uid):
    hotel_obj = Hotel.objects.get(uid = uid)

    if request.method == 'POST':
        checkin = request.POST.get('checkin')
        checkout= request.POST.get('checkout')
        hotel = Hotel.objects.get(uid = uid)
        if not check_booking(checkin ,checkout  , uid , hotel.room_count):
            messages.warning(request, 'Hotel is already booked in these dates ')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

        HotelBooking.objects.create(hotel=hotel , user = request.user , start_date=checkin
        , end_date = checkout , booking_type  = 'Pre Paid')
        
        messages.success(request, 'Your booking has been saved')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))




    return render(request , 'hotel_detail.html' ,{
        'hotels_obj' :hotel_obj
    })


def login_page1(request):
    return render(request,'login_page1.html')



def signin(request):
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']

        user= authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            firstname =user.first_name
            return render(request,'homepage.html',{'firstname':firstname})
        else:
            messages.error(request,'bad credentials')
            return redirect('homepage')

    return render(request,'signin.html')

def signup(request):
    if request.method =='POST':
       username = request.POST['username']
       firstname = request.POST['firstname']
       email = request.POST['email']
       password =request.POST['password']
       password2 = request.POST['password2']

       myuser=User.objects.create_user(username,email,password)
       myuser.firstname = firstname
       myuser.save()
       return redirect('signin')

     
    return render(request,'signup.html')
    





    





   







