class ParsingError(Exception):
    """Parsing error"""

class MissingFieldError(ParsingError):
    """Missing field error"""

class WrongBlankFieldError(ParsingError):
    """Missing blank field"""

class WrongTransitionsFieldsError(ParsingError):
    """Wrong transition error"""

class WrongInitialFieldError(ParsingError):
    """Wrong initial field error"""

class WrongFinalsFieldError(ParsingError):
    """Wrong finals field error"""

class TransitionsDefinitionFieldError(ParsingError):
    """Transition definition field"""

class BlankInInput(ParsingError):
    """Blank char in input"""

class InputCharError(ParsingError):
    """Wrong char in input"""