from django.urls import path, include
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework.routers import DefaultRouter
from users.views.cbv_views import UserCreateView, OrganizationAPIView
from users.views.viewsets import ProfileViewSet, OrganizationViewSet


router = DefaultRouter()
router.register('profiles', ProfileViewSet, basename='')
router.register('organizations', OrganizationViewSet, basename='')

urlpatterns = [
    path('login/', obtain_jwt_token),
    path('register/', UserCreateView.as_view()),
    path('organisations/', OrganizationAPIView.as_view()),
    path('', include(router.urls)),

]

