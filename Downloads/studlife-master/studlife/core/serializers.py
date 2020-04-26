from rest_framework import serializers
from core.models import Post, Event, CommentPost
from users.serializers import CustomUserSerializer, OrganizationSerializer


class PostSerializer(serializers.ModelSerializer):
    owner_name = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Post
        fields = ('id', 'name', 'owner_name')

    def get_owner_name(self, obj):
        return obj.owner.username


class PostDetailedSerializer(serializers.ModelSerializer):
    owner = CustomUserSerializer(read_only=True)

    class Meta(PostSerializer.Meta):
        fields = PostSerializer.Meta.fields + ('owner', 'created_at', 'text')


class EventSerializer(serializers.ModelSerializer):
    organization_name = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Event
        fields = ('id', 'name', 'organization_name')

    def get_organization_name(self, obj):
        return obj.organization.name


class EventDetailedSerializer(serializers.ModelSerializer):
    organization = OrganizationSerializer(read_only=True)

    class Meta(EventSerializer.Meta):
        fields = EventSerializer.Meta.fields + ('organization', 'date', 'description', 'poster')


class CommentPostSerializer(serializers.ModelSerializer):
    post = serializers.SerializerMethodField(read_only=True)
    user_name = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = CommentPost
        fields = ('id', 'message', 'post_name', 'user_name')

    def get_post_name(self, obj):
        return obj.post.name

    def get_user_name(self, obj):
        return obj.user.username


class CommentPostDetailedSerializer(serializers.ModelSerializer):
    post = PostSerializer(read_only=True)
    user = CustomUserSerializer(read_only=True)

    class Meta(CommentPostSerializer.Meta):
        fields = CommentPostSerializer.Meta.fields + ("created_at",)
