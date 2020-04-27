from django.urls import path, include
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework.routers import DefaultRouter
from users.views.cbv_views import UserCreateView
from users.views.viewsets import ProfileViewSet, OrganizationViewSet


router = DefaultRouter()
router.register('profiles', ProfileViewSet, basename='users')
router.register('organizations', OrganizationViewSet, basename='users')

urlpatterns = [
    path('', include(router.urls)),
    path('login/', obtain_jwt_token),
    path('register/', UserCreateView.as_view()),
    path('', include(router.urls)),

] + router.urls

