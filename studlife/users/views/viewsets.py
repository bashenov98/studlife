from django.core.mail import send_mail
from rest_framework.response import Response
from rest_framework import viewsets, mixins
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.parsers import FormParser, MultiPartParser, JSONParser
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from users.models import Profile, Organization
from users.serializers import ProfileSerializer, OrganizationSerializer, ProfileDetailedSerializer, OrganizationDetailedSerializer

class ProfileViewSet(viewsets.GenericViewSet):
    queryset = Profile.objects.all()
    permission_classes = (IsAuthenticated, )

    def get_serializer_class(self):
        if self.action == 'list':
            return ProfileSerializer
        return ProfileDetailedSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        return serializer.data

class OrganizationViewSet(viewsets.GenericViewSet):
    queryset = Organization.objects.all()
    permission_classes = (IsAuthenticated, )

    def get_serializer_class(self):
        if self.action == 'list':
            return OrganizationSerializer
        return OrganizationDetailedSerializer

    def perform_create(self, serializer):
        serializer.save(president=self.request.user)
        return serializer.data
