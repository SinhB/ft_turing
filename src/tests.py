import unittest

from utils.error import (
    MissingFieldError,
    ParsingError,
    TransitionsDefinitionFieldError,
    WrongBlankFieldError,
    WrongFinalsFieldError,
    WrongInitialFieldError,
    WrongTransitionsFieldsError,
)
from utils.health_check import (
    check_blank_field,
    check_finals_field,
    check_initial_field,
    check_machine_fields,
    check_transition_definition,
    check_transitions_fields,
)


class TestHealthCheck(unittest.TestCase):
    def test_missing_fields(self):
        missing_field_json = {
            "name": "unary_sub",
            "alphabet": ["1", ".", "-", "="],
            "blank": ".",
            "states": ["scanright", "eraseone", "subone", "skip", "HALT"],
            "initial": "scanright",
            "transitions": {},
        }
        with self.assertRaises(MissingFieldError):
            check_machine_fields(missing_field_json)

    def test_good_fields(self):
        good_field_json = {
            "name": "unary_sub",
            "alphabet": ["1", ".", "-", "="],
            "blank": ".",
            "states": ["scanright", "eraseone", "subone", "skip", "HALT"],
            "initial": "scanright",
            "finals": {},
            "transitions": {},
        }
        try:
            check_machine_fields(good_field_json)
        except ParsingError:
            self.fail()

    def test_wrong_blank_field(self):
        wrong_blank_field = {
            "alphabet": ["1", ".", "-", "="],
            "blank": ",",
        }
        with self.assertRaises(WrongBlankFieldError):
            check_blank_field(wrong_blank_field)

    def test_good_blank_field(self):
        good_blank_field = {
            "alphabet": ["1", ".", "-", "="],
            "blank": ".",
        }
        try:
            check_blank_field(good_blank_field)
        except ParsingError:
            self.fail()

    def test_wrong_transitions_fields(self):
        wrong_transition_json = {
            "states": ["scanright", "eraseone", "subone", "skip", "HALT"],
            "transitions": {
                "scanlfest": [],
                "eraseone": [],
                "subone": [],
                "skip": [],
            },
        }
        with self.assertRaises(WrongTransitionsFieldsError):
            check_transitions_fields(wrong_transition_json)

    def test_good_transitions_fields(self):
        good_transition_json = {
            "states": ["scanright", "eraseone", "subone", "skip", "HALT"],
            "transitions": {
                "scanright": [],
                "eraseone": [],
                "subone": [],
                "skip": [],
            },
        }
        try:
            check_transitions_fields(good_transition_json)
        except ParsingError:
            self.fail()

    def test_wrong_initial_field(self):
        bad_inital_field = {
            "states": ["scanright", "eraseone", "subone", "skip", "HALT"],
            "initial": "scanleft",
        }
        with self.assertRaises(WrongInitialFieldError):
            check_initial_field(bad_inital_field)

    def test_good_initial_field(self):
        good_inital_field = {
            "states": ["scanright", "eraseone", "subone", "skip", "HALT"],
            "initial": "scanright",
        }
        try:
            check_initial_field(good_inital_field)
        except ParsingError:
            self.fail()

    def test_wrong_finals_field(self):
        wrong_final_field = {
            "states": ["scanright", "eraseone", "subone", "skip", "HALT"],
            "finals": ["HOLT"],
        }
        with self.assertRaises(WrongFinalsFieldError):
            check_finals_field(wrong_final_field)

    def test_good_finals_field(self):
        good_final_field = {
            "states": ["scanright", "eraseone", "subone", "skip", "HALT"],
            "finals": ["eraseone", "HALT"],
        }
        try:
            check_finals_field(good_final_field)
        except ParsingError:
            self.fail()

    def test_missing_transitions_definition_fields(self):
        missing_transition_field_json = {
            "states": ["scanright", "eraseone", "subone", "skip", "HALT"],
            "transitions": {
                "scanright": [],
                "eraseone": [],
                "subone": [],
                "skip": [],
            },
        }
        with self.assertRaises(TransitionsDefinitionFieldError):
            check_transition_definition(missing_transition_field_json)

    def test_wrong_type_transitions_definition_fields(self):
        wrong_type_transition_field_json = {
            "states": ["scanright", "eraseone", "subone", "skip", "HALT"],
            "transitions": {
                "scanright": ["d"],
                "eraseone": [],
                "subone": [],
                "skip": [],
            },
        }
        with self.assertRaises(TransitionsDefinitionFieldError):
            check_transition_definition(wrong_type_transition_field_json)

    def test_wrong_dict_transitions_definition_fields(self):
        wrong_dict_transition_field_json = {
            "states": ["scanright", "eraseone", "subone", "skip", "HALT"],
            "transitions": {
                "scanright": [
                    {
                        "read": ".",
                        "to_state": "scanright",
                        "write": ".",
                        "action": "RIGHT",
                    },
                ],
                "eraseone": [
                    {
                        "read": ".",
                        "TOO_LATE": "scanright",
                        "write": ".",
                        "action": "RIGHT",
                    },
                ],
                "subone": [
                    {
                        "read": ".",
                        "to_state": "scanright",
                        "write": ".",
                        "action": "RIGHT",
                    },
                ],
                "skip": [
                    {
                        "read": ".",
                        "to_state": "scanright",
                        "write": ".",
                        "action": "RIGHT",
                    },
                ],
            },
        }
        with self.assertRaises(TransitionsDefinitionFieldError):
            check_transition_definition(wrong_dict_transition_field_json)

    def test_good_transitions_definition_fields(self):
        good_transition_field_json = {
            "states": ["scanright", "eraseone", "subone", "skip", "HALT"],
            "transitions": {
                "scanright": [
                    {
                        "read": ".",
                        "to_state": "scanright",
                        "write": ".",
                        "action": "RIGHT",
                    },
                ],
                "eraseone": [
                    {
                        "read": ".",
                        "to_state": "scanright",
                        "write": ".",
                        "action": "RIGHT",
                    },
                ],
                "subone": [
                    {
                        "read": ".",
                        "to_state": "scanright",
                        "write": ".",
                        "action": "RIGHT",
                    },
                ],
                "skip": [
                    {
                        "read": ".",
                        "to_state": "scanright",
                        "write": ".",
                        "action": "RIGHT",
                    },
                ],
            },
        }
        try:
            check_transition_definition(good_transition_field_json)
        except ParsingError:
            self.fail()


if __name__ == "__main__":
    unittest.main(verbosity=2)
