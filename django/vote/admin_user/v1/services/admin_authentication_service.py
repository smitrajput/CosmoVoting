from django.db import connection


class AdminAuthentication(object):

    def __init__(self, authentication_data):
        self.session_token = authentication_data.get("session_token")
        self.admin_user_id = authentication_data.get("admin_user_id")
        self.login = self._login()

    def _login_query(self):
        return """SELECT * FROM admin_user_login 
                   WHERE admin_user_id = %s 
                   AND session_token = %s 
                   AND is_active = 1 
                   ORDER BY updated_at DESC;"""

    def _update_login_query(self):
        return """UPDATE admin_user_login 
                    SET updated_at=datetime() 
                    WHERE admin_user_id = %s 
                    AND session_token = %s 
                    AND is_active = 1 ;"""

    def _login(self):
        login_row = None
        with connection.cursor() as cursor:
            cursor.execute(self._login_query(), [
                           self.admin_user_id, self.session_token])
            login_row = cursor.fetchone()
        return login_row

    def is_valid(self):
        is_valid = False
        login_row = self._login()
        if login_row:
            is_valid = True
            with connection.cursor() as cursor:
                cursor.execute(self._update_login_query(), [
                               self.admin_user_id, self.session_token])
        return is_valid
