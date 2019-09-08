from __future__ import unicode_literals
from django.shortcuts import render
# -*- coding: utf-8 -*-
from . import serializers
from django.shortcuts import get_object_or_404
from otp.models import Otp_session
from kyc.models import KycInfo
from constituency.models import Constituency
from polling_booth.models import PollingBooth
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .services.kyc_verfication_service import Kyc
from common.v1.decorators import meta_data_response, session_authorize, catch_exception
from common.v1.utils.error_wrapper import error_wrapper
from django.views.decorators.csrf import csrf_exempt
# from . import serializers



class GetKycList(APIView):
    """
    View for fectching the kyc details.
    """
# @meta_data_response()
    def get(self, request):

        kyc_list = KycInfo.objects.filter(verification_status=False)
        serializer = serializers.KycInfoSerializer(kyc_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class GetKycData(APIView):
    """
    View for fectching the kyc details.
    """
# @meta_data_response()
    def get(self, request, uuid):
        # try:
        #     kyc_data = KycInfo.objects.get(uuid= uuid)

        # except:
        #     kyc_data = {result:"the data for particular user does not exist"}  
        
        kyc_data = get_object_or_404(KycInfo, uuid=uuid)
        serializer = serializers.KycInfoSerializer(kyc_data)

        return Response(serializer.data, status=status.HTTP_200_OK)

class UpdateVoterId(APIView):
    """
    View for fectching the kyc details.
    """
# @meta_data_response()
    def post(self, request):
        # try:
        #     kyc_data = KycInfo.objects.get(uuid= uuid)

        # except:
        #     kyc_data = {result:"the data for particular user does not exist"}  
        
        kyc_data = get_object_or_404(KycInfo, uuid=request.data["uuid"])
        kyc_data.voter_id = request.data["voter_id"]
        kyc_data.save()
        serializer = serializers.KycInfoSerializer(kyc_data)
        return Response(serializer.data, status=status.HTTP_200_OK)


class AddKycData(APIView):
    """
    View for adding the kyc details from the frontend.
    """
    def post(self, request):

        print (request.data)
        consti = get_object_or_404(Constituency, name = request.data["constituency"])
        serializer = serializers.KycInfoSerializer(data=request.data)
        if serializer.is_valid():
            new_voter = serializer.save()
            new_voter.constituency = consti
            new_voter.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({'error': error_wrapper(serializer.errors)},
                        status=status.HTTP_400_BAD_REQUEST)


class VerifyKycData(APIView):
    """
    View for verifying the kyc details. this will be called by a legitimate verifier. 
    """
    def post(self, request):

        print (request.data)
        
        try:
            user = KycInfo.objects.get(uuid = request.data["uuid"])
            print(user)
            user.verification_status = True
            user.save()
            serializer = serializers.KycInfoSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
            
        except :
            return Response({'error': "Can't Process. Please recheck the data again"},
                        status=status.HTTP_400_BAD_REQUEST)



# May will be used for better sematics 

# class VerifyKycData(APIView):
#     """
#     View for verifying the kyc details. this will be called by a legitimate verifier. 
#     """
#     def post(self, request):

#         print (request.data)
#         print(request.data["uuid"])
#         print(request.data["constituency"]) 
        
#         try:
#             user = KycInfo.objects.get(uuid = request.data["uuid"])
#             print(user)
#             print(Constituency.objects.all())
#             constituency = Constituency.objects.get(name=request.data["constituency"])
#             polling_booth = PollingBooth.objects.get(address=request.data["polling_booth"])
#             print(polling_booth)
#             print(constituency)
#             user.constituency = constituency
#             user.polling_booth = polling_booth
#             user.kyc_done = True
#             user.save()
#             serializer = serializers.KycInfoSerializer(user)
#             return Response(serializer.data, status=status.HTTP_200_OK)
            
#         except :
#             return Response({'error': "Can't Process. Please recheck the data again"},
#                         status=status.HTTP_400_BAD_REQUEST)
        
