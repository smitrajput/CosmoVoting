import pyotp
from django.utils.crypto import get_random_string
from rest_framework import serializers

from common.v1.utils.date_format import Date
from user.models import User, Login
from common.v1 import utils, error_messages


STATUS = {
    "ACTIVE": True,
    "INACTIVE": False,
}

TOKEN_EXPIRY_TIME = 45


class ValidateUserLogin(object):

    def __init__(self, login_data):
        self.user_name = login_data.get("user_name", "")
        self.password = login_data.get("password", "")
        self.otp_key = login_data.get("otp_key", 0)
        self.user = self._get_user()

    def _get_user(self):
        return User.objects.filter(user_name=self.user_name, status=STATUS["ACTIVE"]).first()

    def _check_otp_key(self):
        """
        Validates the OTP_key for this User.
            - Return type is boolean
        """
        totp = pyotp.TOTP(self.user.secret_key)
        return totp.verify(self.otp_key)

    def _check_password(self):
        """
        Validates the Password for this User.
            - Return type is boolean
        """
        return utils.encryption_utils.is_match(self.password, self.user.password_hash)

    def perform_tasks(self):
        if not self.user:
            raise serializers.ValidationError(error_messages.WRONG_USER_NAME)
        if not self._check_otp_key():
            raise serializers.ValidationError(error_messages.INVALID_OTP_KEY)
        if not self._check_password():
            raise serializers.ValidationError(error_messages.WRONG_PASSWORD)

    def get_user_id(self):
        return self.user.user_id


class UserLogin(object):

    def __init__(self, user_id):
        self.user_id = user_id
        self.login = self._get_login()

    def _get_login(self):
        return Login.objects.filter(user_id=self.user_id, is_active=STATUS["ACTIVE"]).first()

    def _get_user(self):
        return User.objects.filter(user_id=self.user_id).first()

    def _generate_session_token(self):
        return 'User_' + str(self.user_id) + '_' + get_random_string(length=32)

    def _create_login(self):
        # user = self._get_user()

        login_data = {
            'user_id': self.user_id,
            'session_token': self._generate_session_token(),

        }
        return Login.objects.create(**login_data)

    def _is_session_token_valid(self):
        return (Date.now() - self.login.updated_at).days < TOKEN_EXPIRY_TIME

    def _delete_past_sessions(self):
        """
        Soft deletes the login entry for this user
        """
        Login.objects.filter(session_token=self.login.session_token,
                             user_id=self.user_id,
                             is_active=True
                             ).update(session_token=None, is_active=False)

    def _validate_session(self):
        session_validity = False
        if self._is_session_token_valid():
            session_validity = True
        return session_validity

    def _refresh_present_login(self):
        self.login.is_active = STATUS["ACTIVE"]
        self.login.save()

    def get_session_data(self):
        if not self.login:
            self.login = self._create_login()
        elif not self._validate_session():
            self._delete_past_sessions()
            self.login = self._create_login()
        else:
            self._refresh_present_login()
        return {
            'session_token': self.login.session_token,
            'user_id': self.user_id,
        }


class UserLogout(object):

    def __init__(self, user_id, session_token):
        self.user_id = user_id
        self.session_token = session_token

    def _delete_past_sessions(self):
        """
        Soft deletes the login entry for this user
        """
        Login.objects.filter(session_token=self.session_token,
                             user_id=self.user_id,
                             is_active=True
                             ).update(session_token=None, is_active=False)

    def perform_tasks(self):
        self._delete_past_sessions()
