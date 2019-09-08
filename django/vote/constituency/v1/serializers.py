from rest_framework import serializers
from constituency.models import Constituency
# from .utils.date_format import create_expiry
# from .services.role_service import Moderator_service

# class ConstituencySerializer(serializers.ModelSerializer):

#     has_blocked = serializers.StringRelatedField(many=True, read_only=True)
#     blocked_by = serializers.StringRelatedField(many=True, read_only=True)

#     class Meta:
#         model = ChatProfile
#         fields = '__all__'
#         fields = ('id',  'chat_id', 'user_name', 'is_mod',
#                   'is_allowed', 'is_online', 'has_blocked', 'blocked_by')


class ConstituencySerializer(serializers.ModelSerializer):
    candidates = serializers.StringRelatedField(many=True, read_only=True)
    polling_booths = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Constituency
        fields = ('id', 'name', 'created_at', 'state', 'candidates','polling_booths')

