from django.urls import path
from .views import singupView

urlpatterns = [
    path('signup/', singupView, name='signup'),
]