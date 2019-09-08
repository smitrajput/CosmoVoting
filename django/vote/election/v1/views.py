from __future__ import unicode_literals
from django.shortcuts import render
# -*- coding: utf-8 -*-
from . import serializers
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from election.models import Election

class ElectionList(APIView):
    """
    View for fectching the kyc details.
    """
    def get(self, request):

        elections = Election.objects.all()
        serializer = serializers.ElectionSerializer(elections, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UpdateStatus(APIView):
    """
    View for fectching the kyc details.
    """
    def post(self, request):
        print(request.data)
        election = get_object_or_404(Election, label=request.data["label"])
        election.status = request.data["status"]
        election.save()
        serializer = serializers.ElectionSerializer(election)
        return Response(serializer.data, status=status.HTTP_200_OK)

