from django.shortcuts import render
from .models import Hotel

def hotels(request):
    hotels= Hotel.objects.all()
    return render(request, 'hotels/hotels.html', {'hotels': hotels})
