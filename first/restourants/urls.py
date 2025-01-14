from django.urls import path
from . import views

urlpatterns = [
    path('', views.restaurant_list, name='restourants'),
    path('<int:pk>', views.RestaurantDetailView.as_view(), name='restaurant')
]