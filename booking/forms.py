from django import forms
from hotels.models import HotelRoom

class BookingForm(forms.Form):
    room = forms.ModelChoiceField(
        queryset=HotelRoom.objects.filter(available_count__gt=0),
        required=True,
        label="Room",
        empty_label="Select a room"
    )
    start_date = forms.DateField(widget=forms.DateInput(attrs={"type": "date"}), label="Start Date")
    end_date = forms.DateField(widget=forms.DateInput(attrs={"type": "date"}), label="End Date")
