from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _


class UppercaseValidator:
    def __init__(self, min_value=1):
        self.min_value = min_value

    def validate(self, password, user=None):
        number_of_upper_letters = sum(1 for c in password if c.isupper())

        if number_of_upper_letters < self.min_value:
            raise ValidationError(
                _("This password must contain at least %(min_value)d uppercase letter(s)."),
                code='password_contains_too_few_uppercase_letters',
                params={'min_value': self.min_value},
            )

    def get_help_text(self):
        return _(
            "Your password must contain at least %(min_value)d uppercase letter(s)."
            % {'min_value': self.min_value}
        )


class NumericValidator:
    def __init__(self, min_value=1):
        self.min_value = min_value

    def validate(self, password, user=None):
        number_of_numerics = sum(1 for c in password if c.isnumeric())

        if number_of_numerics < self.min_value:
            raise ValidationError(
                _("This password must contain at least %(min_value)d numeric(s)."),
                code='password_contains_too_few_numbers',
                params={'min_value': self.min_value},
            )

    def get_help_text(self):
        return _(
            "Your password must contain at least %(min_value)d numeric(s)."
            % {'min_value': self.min_value}
        )


class SpecialCharacterValidator:
    def __init__(self, min_value=1):
        self.min_value = min_value

    def validate(self, password, user=None):
        number_of_special_characters = 0
        for letter in password:
            if letter.isalpha():
                continue
            elif letter.isdigit():
                continue
            else:
                number_of_special_characters = number_of_special_characters + 1

        if number_of_special_characters < self.min_value:
            raise ValidationError(
                _("This password must contain at least %(min_value)d special character(s)."),
                code='password_contains_too_few_numbers',
                params={'min_value': self.min_value},
            )

    def get_help_text(self):
        return _(
            "Your password must contain at least %(min_value)d special character(s)."
            % {'min_value': self.min_value}
        )