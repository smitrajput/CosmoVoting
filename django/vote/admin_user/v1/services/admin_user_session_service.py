import pyotp
from django.utils.crypto import get_random_string
from rest_framework import serializers

from common.v1.utils.date_format import Date
from admin_user.models import AdminUser, AdminLogin
from common.v1 import utils, error_messages


STATUS = {
    "ACTIVE": True,
    "INACTIVE": False,
}

TOKEN_EXPIRY_TIME = 45


class ValidateAdminUserLogin(object):

    def __init__(self, admin_login_data):
        self.admin_user_name = admin_login_data.get("admin_user_name", "")
        self.password = admin_login_data.get("password", "")
        self.admin_user = self._get_admin_user()

    def _get_admin_user(self):
        return AdminUser.objects.filter(admin_user_name=self.admin_user_name, status=STATUS["ACTIVE"]).first()

    def _check_password(self):
        """
        Validates the Password for this User.
            - Return type is boolean
        """
        return utils.encryption_utils.is_match(self.password, self.admin_user.password_hash)

    def perform_tasks(self):
        if not self.admin_user:
            raise serializers.ValidationError(error_messages.WRONG_USER_NAME)
        if not self._check_password():
            raise serializers.ValidationError(error_messages.WRONG_PASSWORD)

    def get_admin_user_id(self):
        return self.admin_user.admin_user_id


class AdminUserLogin(object):

    def __init__(self, admin_user_id):
        self.admin_user_id = admin_user_id
        self.admin_login = self._get_admin_login()

    def _get_admin_login(self):
        return AdminLogin.objects.filter(admin_user_id=self.admin_user_id, is_active=STATUS["ACTIVE"]).first()

    def _get_admin_user(self):
        return AdminUser.objects.filter(user_id=self.user_id).first()

    def _generate_session_token(self):
        return 'Admin_' + str(self.admin_user_id) + '_' + get_random_string(length=32)

    def _create_admin_login(self):
        # user = self._get_admin_user()

        admin_login_data = {
            'admin_user_id': self.admin_user_id,
            'session_token': self._generate_session_token(),

        }
        return AdminLogin.objects.create(**admin_login_data)

    def _is_session_token_valid(self):
        return (Date.now() - self.admin_login.updated_at).days < TOKEN_EXPIRY_TIME

    def _delete_past_sessions(self):
        """
        Soft deletes the login entry for this user
        """
        AdminLogin.objects.filter(session_token=self.admin_login.session_token,
                                  admin_user_id=self.admin_user_id,
                                  is_active=True
                                  ).update(session_token=None, is_active=False)

    def _validate_session(self):
        session_validity = False
        if self._is_session_token_valid():
            session_validity = True
        return session_validity

    def _refresh_present_admin_login(self):
        self.admin_login.is_active = STATUS["ACTIVE"]
        self.admin_login.save()

    def get_session_data(self):
        if not self.admin_login:
            self.admin_login = self._create_admin_login()
        elif not self._validate_session():
            self._delete_past_sessions()
            self.admin_login = self._create_admin_login()
        else:
            self._refresh_present_admin_login()
        return {
            'session_token': self.admin_login.session_token,
            'admin_user_id': self.admin_user_id,
        }


class AdminUserLogout(object):

    def __init__(self, admin_user_id, session_token):
        self.admin_user_id = admin_user_id
        self.session_token = session_token

    def _delete_past_sessions(self):
        """
        Soft deletes the login entry for this user
        """
        AdminLogin.objects.filter(session_token=self.session_token,
                             admin_user_id=self.admin_user_id,
                             is_active=True
                             ).update(session_token=None, is_active=False)

    def perform_tasks(self):
        self._delete_past_sessions()
