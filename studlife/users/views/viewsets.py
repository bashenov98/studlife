from django.core.mail import send_mail
from rest_framework.response import Response
from rest_framework import viewsets, mixins
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.parsers import FormParser, MultiPartParser, JSONParser
from rest_framework.permissions import IsAuthenticated, IsAdminUser

<<<<<<< HEAD
from users.models import Profile, Organization
from users.serializers import ProfileSerializer, OrganizationSerializer

class ProfileViewSet(viewsets.GenericViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = (IsAuthenticated)
=======
from users.models import Profile, Organization, CustomUser
from users.serializers import ProfileSerializer, OrganizationSerializer


class ProfileViewSet(viewsets.GenericViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = (IsAuthenticated, )

>>>>>>> asd

class OrganizationViewSet(viewsets.GenericViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
<<<<<<< HEAD
    permission_classes = (IsAuthenticated)
=======
    permission_classes = (IsAuthenticated, )
>>>>>>> asd
