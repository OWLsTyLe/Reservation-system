from django import forms
from .models import Table, Reservation

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['table', 'date', 'time']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.TimeInput(attrs={'type': 'time'}),
        }

    def __init__(self, *args, **kwargs):
        restaurant_id = kwargs.pop('restaurant_id', None)
        super().__init__(*args, **kwargs)

        if restaurant_id:
            self.fields['table'].queryset = Table.objects.filter(restaurant_id=restaurant_id)

        self.fields['table'].widget.attrs.update({'class': 'form-select'})
