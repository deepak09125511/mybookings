from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Event,Booking
from .form import BookingForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .form import customuserform
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from .models import Booking



# Create your views here.

def log_in(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(username = username )
        except User.DoesNotExist:
            messages.error(request,"user does not exist")
            return redirect('login')
        
        authenticated_user = authenticate(request,username = username,password = password)
        
        if authenticated_user is not None:
            login(request,user)
            return redirect('home')
    context ={'page':page}
    return render(request,'login_signup.html',context)

def sign_in(request):
    page = 'signup'
    form = customuserform()
    if request.method == 'POST':
        form = customuserform(request.POST)
        if form.is_valid():
           user = form.save(commit=False)
           user.username = user.username.lower()
           user.is_staff = False
           user.is_superuser = False
           user.save()
           login(request,user)
           return redirect("home")
        messages.error(request,"An error occured during signin")
    return render(request,'login_signup.html',{'form':form})


def log_out(request):
    logout(request)
    return redirect('home')

def home(request):
    events = Event.objects.all()  # Get all events from the database
    return render(request, 'home.html', {'events': events}) 

@login_required(login_url = 'login')
def booking_event(request,event_id):
    event = get_object_or_404(Event,id = event_id)
    form = BookingForm()
    

    if request.method == 'POST':
        form = BookingForm(request.POST)

        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.event = event
            booking.save()
            return redirect('generate_ticket',booking_id = booking.id)
    else:
        form = BookingForm()
    
    return render(request,'booking_event.html',{'form': form, 'event': event})

def generate_ticket(request,booking_id):
    booking = get_object_or_404(Booking,id = booking_id)
    return render(request,'tickets.html',{'booking':booking})







    
