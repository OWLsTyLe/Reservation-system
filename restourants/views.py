from django.shortcuts import render, redirect, get_object_or_404
from .models import Restaurant, Table, Reservation
from .forms import ReservationForm
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView

def restaurant_list(request):
    restaurants = Restaurant.objects.all()
    return render(request, 'restourants/restourants.html', {'restaurants': restaurants})

class RestaurantDetailView(DetailView):
    model = Restaurant
    template_name = 'restourants/restaurant.html'
    context_object_name = 'restaurant'


@login_required
def reservation_view(request, restaurant_id):
    restaurant = get_object_or_404(Restaurant, id=restaurant_id)
    if request.method == 'POST':
        form = ReservationForm(request.POST, restaurant_id = restaurant_id)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.user = request.user
            reservation.save()
            return redirect('reservation_success')

    else:
        form = ReservationForm(restaurant_id=restaurant_id)

    return render(request, 'restourants/restaurant.html', {'form': form, "restaurant": restaurant})

def reservation_success(request):
    return render(request, "main/index.html")