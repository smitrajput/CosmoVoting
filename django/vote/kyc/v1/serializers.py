from rest_framework import serializers

from kyc.models import KycInfo
from .services.kyc_verfication_service import Kyc


class KycInfoSerializer(serializers.ModelSerializer):
    
    constituency = serializers.ReadOnlyField(source='constituency.name')
    polling_booth = serializers.ReadOnlyField(source='polling_booth.address')
    class Meta:
        model = KycInfo
        fields = '__all__'
        # fields = ('id', 'account_name', 'users', 'created')

# class UserRegistrationSerializer(serializers.Serializer):
#     """
#     Custom Serializer to validate and create a new user.
#     """
#     user_name = serializers.CharField(required=True)
#     email = serializers.EmailField(required=False)
#     password = serializers.CharField(
#         min_length=6, max_length=60, required=True)

#     def save(self, **kwargs):
#         """
#         Creates a login session after creating a new user
#             - Returns a 16 character base32 secret.
#             - Compatible with Google Authenticator and other OTP apps
#         """
#         user_profile = user_registration_service.UserRegistartion(
#             self.validated_data).register_and_get_user_profile()
#         return {
#             "profile": user_profile,
#         }


# class AuthenticationSerializer(serializers.Serializer):
#     session_token = serializers.CharField(max_length=64)
#     user_id = serializers.IntegerField()

#     def verify_and_update_session(self):
#         authentication = authentication_service.Authentication(
#             self.validated_data)
#         return authentication.is_valid()


# class UserLoginSerializer(serializers.Serializer):
#     """
#     Custom Serializers to validate and create a Login Session
#     """
#     user_name = serializers.CharField(required=True)
#     password = serializers.CharField(
#         min_length=6, max_length=60, required=True)
#     otp_key = serializers.IntegerField(required=True)

#     def save(self, **kwargs):
#         """
#         Create a new session object or return the old one
#         """
#         validate_user_login = user_session_service.ValidateUserLogin(
#             self.validated_data)
#         validate_user_login.perform_tasks()
#         user_id = validate_user_login.get_user_id()
#         return user_session_service.UserLogin(user_id).get_session_data()


# class UserLogoutSerializer(serializers.Serializer):
#     """
#     custom serializers to Logout the user
#     """

#     def logout_user(self, user_id, session_token):
#         """
#         soft delete the user login session
#         """
#         user_session_service.UserLogout(
#             user_id, session_token).perform_tasks()
