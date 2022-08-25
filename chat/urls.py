from django.urls import path
from . import views

urlpatterns = [ 
    path('<str:user_name>/', views.index, name="index"),
    path('<str:user_name>/<str:room_name>/', views.room, name="room"),
]