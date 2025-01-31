from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import BookingForm
from hotels.models import HotelRoom
from .models import Booking
from django.core.mail import send_mail
from django.conf import settings


def send_booking_confirmation(user_email, booking):
    subject = "Підтвердження бронювання"
    message = f"""
    Вітаємо, {booking.user.username}!

    Ваше бронювання успішно створено.

    Готель: {booking.room.hotel.name}
    Тип номеру: {booking.room.room_type.name}
    Ціна за ніч: {booking.room.price_per_night} грн
    Дата заїзду: {booking.start_date}
    Дата виїзду: {booking.end_date}

    Дякуємо, що обрали наш сервіс!
    """

    send_mail(subject, message, settings.EMAIL_HOST_USER, [user_email])

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

                booking = Booking.objects.create(
                    user=request.user,
                    room=room,
                    start_date=start_date,
                    end_date=end_date
                )

                send_booking_confirmation(request.user.email, booking)
                return redirect('ackount')
            else:
                form.add_error('room', 'The selected room is no longer available.')
    else:
        form = BookingForm()

    return render(request, 'booking/create_booking.html', {'form': form})

