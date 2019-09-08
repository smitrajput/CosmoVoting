from rest_framework import serializers

from candidate.models import Candidate
# from .services.kyc_verfication_service import Kyc


class CandidateSerializer(serializers.ModelSerializer):

    constituency = serializers.ReadOnlyField(source='constituency.name')

    class Meta:
        model = Candidate
        fields = '__all__'

class AddingCandidateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Candidate
        fields = ('candidate_name', 'party','age')        