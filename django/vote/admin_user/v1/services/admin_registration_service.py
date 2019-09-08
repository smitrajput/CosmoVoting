from rest_framework import serializers
from common.v1 import error_messages
from admin_user.models import AdminUser
from common.v1.utils import encryption_utils
from user.v1.services.text_validator import TextValidator

PASSWORD_CHECKLIST = [
    "text_not_starts_with_whitespace",
    "text_not_ends_with_whitespace",
]

ADMIN_USER_NAME_CHECKLIST = [
    "text_is_available_in_the_database",
    "text_length_is_atleast_eight",
    "text_not_starts_with_whitespace",
    "text_not_ends_with_whitespace",
]

STATUS = {
    "ACTIVE": True,
    "INACTIVE": False,
}


class AdminUserRegistartion(object):
    """
    user registeration service
    """

    def __init__(self, user_data):
        self.admin_user_name = user_data.get('admin_user_name')
        self.email = user_data.get('email')
        self.password = user_data.get('password')
        self.password_validation_checklist = PASSWORD_CHECKLIST
        self.admin_user_name_validaton_checklist = ADMIN_USER_NAME_CHECKLIST

    def _get_password_hash(self):
        """
        set password for the user.
        """
        return encryption_utils.hash_password(self.password)

    def _check_password_constrain(self):
        return TextValidator(self.password,
                             self.password_validation_checklist
                             ).check_text()

    def _check_admin_user_name_constrain(self):
        return TextValidator(self.admin_user_name,
                             self.admin_user_name_validaton_checklist
                             ).check_text()

    def _register_admin_user(self):
        is_admin_user_name_valid = self._check_admin_user_name_constrain()
        is_password_valid = self._check_password_constrain()
        if not is_admin_user_name_valid:
            raise serializers.ValidationError(
                error_messages.INVALID_admin_USER_NAME)
        if not is_password_valid:
            raise serializers.ValidationError(error_messages.INVALID_PASSWORD)
        new_admin_user = AdminUser.objects.create(
            admin_user_name=self.admin_user_name,
            email=self.email,
            password_hash=self._get_password_hash(),
            status=STATUS["ACTIVE"]
        )
        new_admin_user.save()
        return new_admin_user

    def _new_admin_user_profile(self, new_admin_user):
        return {
            "admin_user_id": new_admin_user.admin_user_id,
            "email": new_admin_user.email,
            "admin_user_name": new_admin_user.admin_user_name
        }

    def register_and_get_user_profile(self):
        new_admin_user = self._register_admin_user()
        user_profile = self._new_admin_user_profile(new_admin_user)
        return user_profile
