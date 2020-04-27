from django.shortcuts import render

from rest_framework import generics
from rest_framework.permissions import AllowAny

from users.models import CustomUser
from users.serializers import CustomUserSerializer
# Create your views here.

<<<<<<< HEAD
=======

>>>>>>> asd
class UserCreateView(generics.CreateAPIView):
    permission_classes = (AllowAny, )
    authentication_classes = ()

    def get_queryset(self):
        return CustomUser.objects.all()

    def get_serializer_class(self):
<<<<<<< HEAD
        return CustomUserSerializer
=======
        return CustomUserSerializer
>>>>>>> asd
