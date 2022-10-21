class ParsingError(Exception):
    """Parsing error"""

    def __init__(self, message: str, value=None) -> None:
        super().__init__()
        self.message = message
        self.values = value

    def __str__(self) -> str:
        return f"{self.message}: {self.values}"


class MissingFieldError(ParsingError):
    """Missing field error"""


class AlphabetLenValueError(ParsingError):
    """Alphabet value not equal to 1"""


class WrongBlankFieldError(ParsingError):
    """Missing blank value"""


class WrongTransitionsFieldsError(ParsingError):
    """Wrong transition error"""


class WrongInitialFieldError(ParsingError):
    """Wrong initial field error"""


class WrongFinalsFieldError(ParsingError):
    """Wrong finals field error"""


class TransitionsDefinitionFieldError(ParsingError):
    """Transition definition field"""

class TransitionValueError(ParsingError):
    """Transition values"""

class BlankInInput(ParsingError):
    """Blank char in input"""


class InputCharError(ParsingError):
    """Wrong char in input"""
