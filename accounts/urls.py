from django.urls import path
from .views import SignupAPView, LoginAPView, logoutView

urlpatterns = [
    path('signup/', SignupAPView.as_view(), name='signup'),
    path('login/', LoginAPView.as_view(), name='login'),
    path('logout/', logoutView, name='logout'),

]