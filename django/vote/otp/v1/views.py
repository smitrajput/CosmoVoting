from __future__ import unicode_literals
from django.shortcuts import render
# -*- coding: utf-8 -*-
from kyc.models import KycInfo
from otp.models import Otp_session
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .services.otp import Otp
from common.v1.decorators import meta_data_response, session_authorize, catch_exception
from common.v1.utils.error_wrapper import error_wrapper
# from . import serializers




class SendOtp(APIView):
    """
    View for the Registration API.
    """
# @meta_data_response()
    def get(self, request, mob_number):
        # serializer = serializers.UserRegistrationSerializer(data=request.data)
        print (mob_number)
        result = Otp().send_otp(mob_number)
        print ("inside the view")
        print (result)
        # try:
        #     otp = Otp_session.objects.get(mobile= mob_number)
        #     otp.session_id = result.get('Details')
        #     otp.save()
        # except:
        #     Otp_session.objects.create(mobile= mob_number, session_id= result.get('Details'))
        
        return Response(result, status=status.HTTP_200_OK)

class SendOtpUuid(APIView):
    """
    View for the Registration API.
    """
# @meta_data_response()
    def get(self, request, uuid):

        result = Otp().send_otp_uuid(uuid)
        return Response(result, status=status.HTTP_200_OK)

class VerifyOtp(APIView):
    """
    View for the Registration API.
    """
# @meta_data_response()
    def get(self, request, mob_number, otp):
        
        print (mob_number)  
        print (otp)
        result = Otp().verify_otp(mob_number, otp)
        print ("inside the view")
        print (result)
        return Response(result, status=status.HTTP_200_OK)

class VerifyOtpUuid(APIView):
    """
    View for the Registration API.
    """
# @meta_data_response()
    def get(self, request, uuid, otp):

        print (uuid) 
        print (otp)
        result = Otp().verify_otp_uuid(uuid, otp)
        print (result)
        return Response(result, status=status.HTTP_200_OK)

# class UserLogin(APIView):
#     """
#     View for UserLogin
#     """
#     # @catch_exception()
#     @meta_data_response()
#     def post(self, request):
#         serializer = serializers.UserLoginSerializer(data=request.data)
#         if serializer.is_valid():
#             session_data = serializer.save()
#             return Response(session_data, status=status.HTTP_200_OK)
#         print(serializer.errors, 100)
#         return Response({'error': error_wrapper(serializer.errors)},
#                         status=status.HTTP_401_UNAUTHORIZED)


# class UserLogout(APIView):
#     """
#     View for User Logout
#     """
#     @meta_data_response()
#     @session_authorize(user_id_key="user_id")
#     def post(self, request, auth_data):
#         if auth_data.get('authorized'):
#             serializer = serializers.UserLogoutSerializer(data=request.data)
#             serializer.logout_user(
#                 user_id=auth_data.get('user_id'),
#                 session_token=auth_data.get('session_token'))
#             return Response({}, status.HTTP_200_OK)
#         return Response({}, status.HTTP_401_UNAUTHORIZED)
