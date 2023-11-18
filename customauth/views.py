from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.hashers import make_password
from django.shortcuts import render

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework import permissions
from rest_framework import viewsets
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token

from .serializers import PhoneSerializer, TokenSerializer
from .authentication import TokenAuthentication

from datetime import datetime, timedelta
import pytz
import os
from twilio.rest import Client
import twilio
import secrets
import string

User = get_user_model()

account_sid = 'ACc11bb124b1aac031415d29c89b6d829a'
auth_token = 'd8b0b2826f2ce7f9d1b66ef95bf66d60'
client = Client(account_sid, auth_token)

@api_view(['GET'])
def api_root(request):
    return Response({
        'Generate-OTP': reverse('generate-otp',  request=request),
        'Verify-OTP': reverse('verify-otp', request=request),
        'logout': reverse('logout', request=request)
    })

def generate_otp():
  while True:
    otp = ''.join([secrets.choice(string.digits) for i in range(4)])
    if len(set(otp)) < len(otp):
        continue

    if '0' in otp or '1' in otp:
        continue 

    return otp

class GenerateOTPView(APIView):
    def post(self,request):
        permission_classes = [permissions.AllowAny]
        serializer = PhoneSerializer(data=request.data)
        if serializer.is_valid():
            phone = serializer.validated_data['phone']
            otp = generate_otp()
            user = User.objects.get(phone=phone)
            user.password = make_password(otp)
            user.save()
            
            message = client.messages.create(
                              from_='+15343445070',
                              body=f'Welcome to HairCo! Please use the OTP below to login to your account.\n{otp}\nThis OTP is valid for 10 minutes. Please do not share it with anyone.\nThank you for choosing HairCo',
                              to='+917903062804'
                          )
            return Response({'generated_otp': otp})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class VerifyOTPView(ObtainAuthToken):
    def post(self, request):
        permission_classes = [permissions.AllowAny]
        serializer = TokenSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            token, created =  Token.objects.get_or_create(user=serializer.validated_data['user'])

            if not created:
                token.created = datetime.now(pytz.UTC)
                token.save()

            return Response({'token': token.key})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LogoutView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        try:
            request.user.auth_token.delete()
            logout(request)
            return Response({
                'message': 'Logout successfully',
                'status': status.HTTP_200_OK,
            })
        except Exception as e:
            return Response({
                'message': str(e),
                'status': status.HTTP_400_BAD_REQUEST,
            })
