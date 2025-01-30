from django.urls import path
from . import views

urlpatterns = [
    path('', views.restaurant_list, name='restourants'),
    path('<int:pk>', views.RestaurantDetailView.as_view(), name='restaurant'),
    path("reservation/<int:restaurant_id>/",  views.reservation_view, name="reservation"),
    path("reservation/success/", views.reservation_success, name="reservation_success"),
]