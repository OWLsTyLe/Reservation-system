from django.shortcuts import render
from booking.models import Booking

def index(request):
    return render(request, 'main/index.html')

def account(request):
    bookings = Booking.objects.filter(user=request.user).select_related('room', 'room__hotel', 'room__room_type')
    return render(request, 'booking/acount.html', {'bookings': bookings})
