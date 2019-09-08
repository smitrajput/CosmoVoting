from rest_framework import serializers

from polling_booth.models import PollingBooth
# from .services.kyc_verfication_service import Kyc


class PollingBoothSerializer(serializers.ModelSerializer):

    constituency = serializers.ReadOnlyField(source='constituency.name')

    class Meta:
        model = PollingBooth
        fields = '__all__'


class AddingPollingBoothSerializer(serializers.ModelSerializer):

    class Meta:
        model = PollingBooth
        fields = ('address', 'officer')        