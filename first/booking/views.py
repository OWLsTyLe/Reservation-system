from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import BookingForm
from hotels.models import HotelRoom
from .models import Booking

@login_required
def create_booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            room = form.cleaned_data['room']
            start_date = form.cleaned_data['start_date']
            end_date = form.cleaned_data['end_date']

            if room.available_count > 0:
                room.available_count -= 1
                room.save()

                Booking.objects.create(
                    user=request.user,
                    room=room,
                    start_date=start_date,
                    end_date=end_date
                )
                return redirect('home')
            else:
                form.add_error('room', 'The selected room is no longer available.')
    else:
        form = BookingForm()

    return render(request, 'booking/create_booking.html', {'form': form})





















