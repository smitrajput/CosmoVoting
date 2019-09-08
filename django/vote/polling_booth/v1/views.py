from django.shortcuts import render
from .serializers import PollingBoothSerializer
from rest_framework import generics
from polling_booth.models import PollingBooth
# Create your views here.


class PollingBoothList(generics.ListCreateAPIView):
    queryset = PollingBooth.objects.all()
    serializer_class = PollingBoothSerializer


class PollingBoothDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PollingBooth.objects.all()
    serializer_class = PollingBoothSerializer
# Create your views here.
