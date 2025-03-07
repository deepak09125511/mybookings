from django import forms
from .models import Booking
from .models import User
from django.contrib.auth.forms import UserCreationForm

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['participant_name','num_tickets','age','sex']
        widgets = {
            'sex': forms.Select(attrs={'class': 'form-control'}),  # ✅ Force dropdown UI
        }

class customuserform(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ['username','email','password1','password2']


