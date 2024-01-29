from django.shortcuts import render,redirect
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.

class SignupSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    confirm_password = serializers.CharField()

    def validate(self, data):
        #check if username exists
        username = data.get('username')
        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError('Username already exists')
        
        #check password and confirm password match
        password = data.get('password')
        confirm_password = data.get('confirm_password')
        if password != confirm_password:
            raise serializers.ValidationError('Passwords do not match')
        return data
    

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

  



class SignupAPView(APIView):
    def get(self, request):
        template_name = 'accounts/signup.html'
        return render(request, template_name)
    
    def post(self, request):
        serializer = SignupSerializer(data=request.data)
        if serializer.is_valid():
            #create User
            user = User.objects.create_user(username=serializer.data['username'], password=serializer.data['password'])
            #make it active
            user.is_active = True
            user.save()
            return Response({'status':'success'})
        return Response(serializer.errors)
    

class LoginAPView(APIView):
    def get(self, request):
        template_name = 'accounts/login.html'
        return render(request, template_name)
    
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            #login user
            user = authenticate(username=serializer.data['username'], password=serializer.data['password'])
            if user is None:
                return Response({'status':'fail'})
            login(request, user)
            return Response({'status':'success'})
        return Response(serializer.errors)
    
@login_required(login_url='/login/')
def logoutView(request):
    logout(request)
    return redirect('login')
