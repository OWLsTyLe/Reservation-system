from django.shortcuts import render
from .models import Restaurant
from django.views.generic import DetailView

def restaurant_list(request):
    restaurants = Restaurant.objects.all()
    return render(request, 'restourants/restourants.html', {'restaurants': restaurants})

class RestaurantDetailView(DetailView):
    model = Restaurant
    template_name = 'restourants/restaurant.html'
    context_object_name = 'restaurant'