from django.urls import path
from .views import indexView,roomsView,roomDetailsView
urlpatterns = [
    path('', indexView, name='index'),
    path('rooms/', roomsView, name='rooms'),

    path('room/<slug>/', roomDetailsView, name='room-details'),
]