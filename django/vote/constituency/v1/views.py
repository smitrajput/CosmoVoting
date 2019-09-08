from django.shortcuts import render
from constituency.v1.serializers import ConstituencySerializer
from rest_framework import generics
from constituency.models import Constituency
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from polling_booth.v1.serializers import AddingPollingBoothSerializer,PollingBoothSerializer
from kyc.models import KycInfo
from rest_framework import status
from candidate.v1.serializers import CandidateSerializer, AddingCandidateSerializer
from rest_framework.response import Response
from common.v1.decorators import meta_data_response, session_authorize, catch_exception
from common.v1.utils.error_wrapper import error_wrapper
# Create your views here.


class ConstituencyList(generics.ListCreateAPIView):
    queryset = Constituency.objects.all()
    serializer_class = ConstituencySerializer


class ConstituencyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Constituency.objects.all()
    serializer_class = ConstituencySerializer


class AddBooth(APIView):
    """
    View for adding a polling booth to a constituency API.
    """
    def post(self, request, constituency_id):

        consti = get_object_or_404(Constituency, id = constituency_id)
        print (request.data)
        serializer = AddingPollingBoothSerializer(data=request.data)
        if serializer.is_valid():
            new_booth =  (serializer.save())
            new_booth.constituency = consti
            new_booth.save()
            new_serializer = PollingBoothSerializer(new_booth)
            print (new_booth.constituency)
            print(serializer.validated_data)
            return Response(new_serializer.data, status=status.HTTP_200_OK)
        return Response({'error': error_wrapper(serializer.errors)},
                        status=status.HTTP_400_BAD_REQUEST)


class CandidateList(APIView):
    """
    View for adding a polling booth to a constituency API.
    """
    def get(self, request, name):
        
        # try:
        consti = get_object_or_404(Constituency, name = name)
        print (consti)
        candidates = consti.candidates.all()
        print(candidates)
        serializer = CandidateSerializer(candidates, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class AddCandidate(APIView):
    """
    View for adding a candidate to a constituency API.
    """
    def post(self, request, constituency_id):

        consti = get_object_or_404(Constituency, id = constituency_id)
        print (request.data)
        serializer = AddingCandidateSerializer(data=request.data)
        if serializer.is_valid():
            new_candidate =  (serializer.save())
            new_candidate.constituency = consti
            new_candidate.save()
            new_serializer = CandidateSerializer(new_candidate)
            print (new_candidate.constituency)
            print(serializer.validated_data)
            return Response(new_serializer.data, status=status.HTTP_200_OK)
        return Response({'error': error_wrapper(serializer.errors)},
                        status=status.HTTP_400_BAD_REQUEST)
