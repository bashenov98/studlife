from rest_framework.permissions import IsAuthenticated, BasePermission


class PostPermission(BasePermission):

    def has_permission(self, request, view):
        if view.action in ['list', 'retrieve']:
            return request.user.is_authenticated
        return True

    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser or request.user.is_staff:
            return True
        if view.action in ['update', 'partial_update', 'destroy']:
            return request.user == obj.owner
        return True


class CommentPermission(BasePermission):

    def has_permission(self, request, view):
        if view.action in ['list', 'retrieve']:
            return request.user.is_authenticated
        return True

    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser or request.user.is_staff:
            return True
        if view.action in ['update', 'partial_update', 'destroy']:
            return request.user == obj.user
        return True


class EventPermission(BasePermission):

    def has_permission(self, request, view):
        if view.action in ['list', 'retrieve']:
            return request.user.is_authenticated
        return True

    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser or request.user.is_staff:
            return True
        if view.action in ['update', 'partial_update', 'destroy']:
            return request.user == obj.organization.president
        return True
