from django.urls import path
from .views import GenerateOTPView, VerifyOTPView, LogoutView, api_root, UserAppointmentViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('users/(?P<user_id>\d+)/appointments', 
                UserAppointmentViewSet, 
                basename='user-appointments')

urlpatterns = [
    path('', api_root, name='auth'),
    path('generate/', GenerateOTPView.as_view(), name='generate-otp'),
    path('verify/', VerifyOTPView.as_view(), name='verify-otp'),
    path('logout/', LogoutView.as_view(), name='logout'),
] + router.urls

