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
    user_name = serializers.SerializerMethodField(read_only=True)
    organization_name = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Profile
        fields = ('id', 'user_name', 'organization_name')

    def get_user_name(self, obj):
        return obj.user.name

    def get_organization_name(self, obj):
        return obj.organization.name

class ProfileDetailedSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer(read_only=True)

    class Meta(ProfileSerializer.Meta):
        fields = ProfileSerializer.Meta.fields + ('avatar', 'bio', 'faculty')


class OrganizationSerializer(serializers.ModelSerializer):
    president_name = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Organization
        fields = ('id', 'name', 'president_name')

    def get_president_name(self, obj):
        return obj.president.name

class OrganizationDetailedSerializer(serializers.ModelSerializer):
    president = CustomUserSerializer(read_only=True)

    class Meta(OrganizationSerializer.Meta):
        fields = OrganizationSerializer.Meta.fields + ('president', 'description', 'image')