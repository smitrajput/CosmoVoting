import string

from user.models import User


class TextValidator(object):

    def __init__(self, to_validate_text, checklist):
        self.to_validate_text = to_validate_text
        self.checklist = checklist
        self.functions_to_check_text = {
            "text_is_available_in_the_database":
                self._user_name_available(self.to_validate_text),
            "text_length_is_atleast_eight":
                self._user_name_length_is_atleast_eight(self.to_validate_text),
            "text_not_starts_with_whitespace":
                self._not_starts_with_whitespace(self.to_validate_text),
            "text_not_ends_with_whitespace":
                self._not_ends_with_whitespace(self.to_validate_text),
            "text_contains_atleast_one_number":
                self._contains_number(self.to_validate_text),
            "text_contains_atleast_one_special_character":
                self._contains_special_char(self.to_validate_text),
            "text_contains_atleast_one_lower_case_chacracter":
                self._contains_lower_case_char(self.to_validate_text),
            "text_contains_atleast_one_upper_case_chacracter":
                self._contains_upper_case_char(self.to_validate_text)
        }

    def _not_starts_with_whitespace(self, to_validate_text):
        if to_validate_text[0] == " ":
            return False
        else:
            return True

    def _not_ends_with_whitespace(self, to_validate_text):
        text_length = len(to_validate_text)
        if to_validate_text[text_length - 1] == " ":
            return False
        else:
            return True

    def _contains_number(self, to_validate_text):
        return any(char.isdigit() for char in to_validate_text)

    def _contains_special_char(self, to_validate_text):
        special_chars = set(string.punctuation)
        return any(char in special_chars for char in to_validate_text)

    def _contains_upper_case_char(self, to_validate_text):
        return any(char.isupper() for char in to_validate_text)

    def _contains_lower_case_char(self, to_validate_text):
        return any(char.islower() for char in to_validate_text)

    def _user_name_available(self, to_validate_text):
        user_name_exists = User.objects.filter(
            user_name=to_validate_text).first()
        return True if user_name_exists is None else False

    def _user_name_length_is_atleast_eight(self, to_validate_text):
        user_name_length = len(to_validate_text)
        return True if user_name_length >= 8 else False

    def check_text(self):
        is_text_valid = True
        for check in self.checklist:
            is_text_valid = is_text_valid \
                and self.functions_to_check_text[check]
        return is_text_valid
