from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Event(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateField()
    location = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)

    def __str__(self):
        return f"{self.name} - {self.location} ({self.date})"

class Booking(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)#links to the registered user 
    event = models.ForeignKey(Event,on_delete=models.CASCADE)#links to the event
    participant_name = models.CharField(max_length=255,default="unknown") 
    age = models.PositiveIntegerField(default=18) 
    sex = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')],default='Male')
    num_tickets = models.PositiveIntegerField(default=1)
    booked_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} booked {self.num_tickets} tickets for {self.event} on {self.booked_on}"
