from django.shortcuts import render
from rest_framework import generics

from .models import CustomUser
from .serializers import UserRegistrationSerializer

# Create your views here.
class CustomUserRegistrationView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserRegistrationSerializer
