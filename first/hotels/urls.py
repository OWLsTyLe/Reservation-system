from django.urls import path
from . import views

urlpatterns = [
    path('', views.hotels, name='hotels'),
    path('<int:pk>', views.HotelDetailView.as_view(), name='din')
]