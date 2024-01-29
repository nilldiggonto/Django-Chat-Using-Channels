from django.shortcuts import render
from .models import ChatRoom
from django.contrib.auth.decorators import login_required

# Create your views here.
def indexView(request):
    return render(request, 'chat/homepage.html')

@login_required(login_url='/login/')
def roomsView(request):
    rooms = ChatRoom.objects.all()
    return render(request, 'chat/rooms.html',{'rooms':rooms})

@login_required(login_url='/login/')
def roomDetailsView(request,slug):
    room = ChatRoom.objects.get(slug=slug)
    return render(request, 'chat/room.html',{'room':room})