from rest_framework import serializers

from users.models import CustomUser, Profile, Organization


class CustomUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = '__all__'

    def create(self, validated_data):
        user = CustomUser.objects.create_user(username=validated_data['username'])

        user.set_password(validated_data['password'])

        user.save()

        return user


class ProfileSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer(read_only=True)

    class Meta:
        model = Profile
        fields = '__all__'


class OrganizationSerializer(serializers.ModelSerializer):
    president = CustomUserSerializer(read_only=True)

    class Meta:
        model = Organization
        fields = '__all__'

    def create(self, validated_data):
        organization = Organization.objects.create_user(username=validated_data['username'])

        organization.set_password(validated_data['password'])

        organization.save()

        return organization
