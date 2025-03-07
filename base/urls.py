from django.urls import path
from .import views


urlpatterns = [
    path('',views.home,name ='home'),
    path('book/<int:event_id>/',views.booking_event,name='booking_event'),
    path('login/',views.log_in,name='login'),
    path('signin/',views.sign_in,name='signin'),
    path('logout/',views.log_out,name='logout'),
    path('generateticket/<int:booking_id>/',views.generate_ticket,name='generate_ticket')
]