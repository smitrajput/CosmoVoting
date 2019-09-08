import pyotp
from rest_framework import serializers
from common.v1 import error_messages
from user.models import User
from common.v1.utils import encryption_utils
from . text_validator import TextValidator

PASSWORD_CHECKLIST = [
    "text_not_starts_with_whitespace",
    "text_not_ends_with_whitespace",
    "text_contains_atleast_one_number",
    "text_contains_atleast_one_special_character",
    "text_contains_atleast_one_lower_case_chacracter",
    "text_contains_atleast_one_upper_case_chacracter",
]

USER_NAME_CHECKLIST = [
    "text_is_available_in_the_database",
    "text_length_is_atleast_eight",
    "text_not_starts_with_whitespace",
    "text_not_ends_with_whitespace",
    "text_contains_atleast_one_number",
    "text_contains_atleast_one_special_character",
    "text_contains_atleast_one_lower_case_chacracter",
    "text_contains_atleast_one_upper_case_chacracter",
]

STATUS = {
    "ACTIVE": True,
    "INACTIVE": False,
}


class UserRegistartion(object):
    """
    user registeration service
    """

    def __init__(self, user_data):
        self.user_name = user_data.get('user_name')
        self.email = user_data.get('email')
        self.password = user_data.get('password')
        self.secret_key = pyotp.random_base32()
        self.password_validation_checklist = PASSWORD_CHECKLIST
        self.user_name_validaton_checklist = USER_NAME_CHECKLIST

    def _get_password_hash(self):
        """
        set password for the user.
        """
        return encryption_utils.hash_password(self.password)

    def _check_password_constrain(self):
        return TextValidator(self.password,
                             self.password_validation_checklist
                             ).check_text()

    def _check_user_name_constrain(self):
        return TextValidator(self.user_name,
                             self.user_name_validaton_checklist
                             ).check_text()

    def _register_user(self):
        """
        Registers the User.
        """
        is_user_name_valid = self._check_user_name_constrain()
        is_password_valid = self._check_password_constrain()
        if not is_user_name_valid:
            raise serializers.ValidationError(error_messages.INVALID_USER_NAME)
        if not is_password_valid:
            raise serializers.ValidationError(error_messages.INVALID_PASSWORD)
        new_user = User.objects.create(
            user_name=self.user_name,
            email=self.email,
            password_hash=self._get_password_hash(),
            secret_key=self.secret_key,
            status=STATUS["ACTIVE"]
        )
        new_user.save()
        return new_user

    def _new_user_profile(self, new_user):
        return {
            "user_id": new_user.user_id,
            "secret_key": new_user.secret_key,
            "email": new_user.email,
            "user_name": new_user.user_name
        }

    def register_and_get_user_profile(self):
        new_user = self._register_user()
        user_profile = self._new_user_profile(new_user)
        return user_profile
