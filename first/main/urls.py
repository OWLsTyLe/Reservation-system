from django.urls import path
from. import views

urlpatterns = [
    path('', views.index, name='home'),
    path('ackount', views.account, name='ackount')
]