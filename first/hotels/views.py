from django.shortcuts import render
from .models import Hotel
from django.views.generic import DetailView

def hotels(request):
    hotels= Hotel.objects.all()
    return render(request, 'hotels/hotels.html', {'hotels': hotels})

class HotelDetailView(DetailView):
    model = Hotel
    template_name = 'hotels/hotel.html'
    context_object_name = 'hotels'