# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from common.v1.responses import MetaDataResponse
from common.v1.decorators import meta_data_response, admin_session_authorize, catch_exception
from common.v1.utils.error_wrapper import error_wrapper
from .services import config_service
from . import serializers


class AdminUserRegistration(APIView):

    @meta_data_response()
    def post(self, request):
        serializer = serializers.AdminUserRegistrationSerializer(
            data=request.data)
        if serializer.is_valid():
            session_data = serializer.save()
            return Response(session_data, status=status.HTTP_200_OK)
        return Response({'error': error_wrapper(serializer.errors)},
                        status=status.HTTP_400_BAD_REQUEST)


class AdminUserLogin(APIView):
    # @catch_exception()

    @meta_data_response()
    def post(self, request):
        serializer = serializers.AdminUserLoginSerializer(data=request.data)
        if serializer.is_valid():
            session_data = serializer.save()
            return Response(session_data, status=status.HTTP_200_OK)
        return Response({'error': error_wrapper(serializer.errors)},
                        status=status.HTTP_401_UNAUTHORIZED)


class AdminUserLogout(APIView):

    @meta_data_response()
    @admin_session_authorize(admin_user_id_key="admin_user_id")
    def post(self, request, auth_data):
        if auth_data.get('authorized'):
            serializer = serializers.AdminUserLogoutSerializer(
                data=request.data)
            serializer.logout_admin_user(
                admin_user_id=auth_data.get('admin_user_id'),
                session_token=auth_data.get('session_token'))
            return Response({}, status.HTTP_200_OK)
        return Response({}, status.HTTP_401_UNAUTHORIZED)


class Config(APIView):

    def get(self, request):
        return MetaDataResponse(config_service.Config().get_config(),
                                status=status.HTTP_200_OK)
