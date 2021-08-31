from django.shortcuts import render

from django.contrib.auth import models
from django.shortcuts import render,redirect
from django.http import JsonResponse

from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.decorators import api_view
from rest_framework.permissions import AllowAny
from django.contrib import messages
# Userlogin signup, import
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import ListView

# Create your views here.
def chatView(request,roomname):
    user=request.user
    print(user)
    roomname=roomname
    rooms=user.group_chats.all()
    context={
        'usr':request.user,
        'rooms':rooms,
        'roomname':roomname
    }
    return render(request,'chatpage.html',context)


def LoginView(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            print("post method called")
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            print(username, password)
            
            if user is not None:
                login(request, user)
                print(user)
                messages.success(
                    request, f"You are now logged in as {username}") 
                
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request,
                  template_name="login.html",
                  context={"form": form})

def LogoutView(request):
    logout(request)
    messages.success(request, "Successfully logged out!")
    return redirect('login')