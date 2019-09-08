from rest_framework import serializers

from admin_user.models import AdminLogin
from . services import admin_user_session_service, admin_authentication_service, admin_registration_service


class AdminUserRegistrationSerializer(serializers.Serializer):
    admin_user_name = serializers.CharField(required=True)
    email = serializers.EmailField(required=False)
    password = serializers.CharField(
        min_length=6, max_length=60, required=True)

    def save(self, **kwargs):
        admin_user_profile = admin_registration_service.AdminUserRegistartion(
            self.validated_data).register_and_get_user_profile()
        return {
            "profile": admin_user_profile,
        }


class AdminAuthenticationSerializer(serializers.Serializer):
    session_token = serializers.CharField(max_length=64)
    admin_user_id = serializers.IntegerField()

    def verify_and_update_session(self):
        authentication = admin_authentication_service.AdminAuthentication(
            self.validated_data)
        return authentication.is_valid()


class AdminUserLoginSerializer(serializers.Serializer):
    admin_user_name = serializers.CharField(required=True)
    password = serializers.CharField(
        min_length=6, max_length=60, required=True)

    def save(self, **kwargs):
        validate_admin_user_login = admin_user_session_service.ValidateAdminUserLogin(
            self.validated_data)
        validate_admin_user_login.perform_tasks()
        admin_user_id = validate_admin_user_login.get_admin_user_id()
        return admin_user_session_service.AdminUserLogin(admin_user_id).get_session_data()


class AdminUserLogoutSerializer(serializers.Serializer):

    def logout_admin_user(self, admin_user_id, session_token):
        admin_user_session_service.AdminUserLogout(
            admin_user_id, session_token).perform_tasks()


class ConfigValueSerializers(serializers.Serializer):

    def get_all_data(self, attribute_name):
        return Configvalue().get_name_value_dict()
