import json

from utils.error import (
    AlphabetLenValueError,
    BlankInInput,
    InputCharError,
    MissingFieldError,
    TransitionsDefinitionFieldError,
    TransitionValueError,
    WrongBlankFieldError,
    WrongFinalsFieldError,
    WrongInitialFieldError,
    WrongTransitionsFieldsError,
)


def print_pretty_json(json_dict):
    """Print beauty json"""
    print(json.dumps(json_dict, indent=4))


def checks(arguments):
    """Checks arguments"""
    if hasattr(arguments, "input"):
        return input_check(health_check(arguments.jsonfile), arguments.input)
    return health_check(arguments.jsonfile)


def health_check(jsonfile: dict):
    """Perform health check of the machine description"""
    with open(jsonfile, encoding="utf-8") as machine_description:
        machine = json.load(machine_description)
        check_machine_fields(machine)
        check_alphabet_field(machine)
        check_blank_field(machine)
        check_transitions_fields(machine)
        check_initial_field(machine)
        check_finals_field(machine)
        check_transition_definition(machine)
        check_transition_values(machine)
    return machine


def input_check(machine: dict, input: str):
    """Check input format"""
    if any(char in input for char in machine["blank"]):
        raise BlankInInput("Blank char in input", set(machine["blank"]))
    if not check_fields(input, machine["alphabet"]):
        raise InputCharError(
            "Wrong char in input", set(input) - set(machine["alphabet"])
        )
    return machine, input


def check_fields(lookup, fields):
    """Return True if all item in lookup are in fields"""
    return all(field in fields for field in lookup)


def check_machine_fields(machine: dict):
    """Check if all required_fields are in the machine"""
    required_fields = [
        "name",
        "alphabet",
        "blank",
        "states",
        "initial",
        "finals",
        "transitions",
    ]
    if not check_fields(required_fields, machine):
        raise MissingFieldError(
            "Missing fields in machine description",
            set(required_fields) - set(machine),
        )


def check_alphabet_field(machine: dict):
    """Check if all values in alphabet are equals to 1"""
    if any(len(char) != 1 for char in machine["alphabet"]):
        raise AlphabetLenValueError(
            "Wrong len for char in alphabet field",
            set(char for char in machine["alphabet"] if len(char) != 1),
        )


def check_blank_field(machine: dict):
    """Check if the blank value is in the alphabet field"""
    if len(machine["blank"]) != 1:
        raise WrongBlankFieldError(
            "Blank field contains more than one value", set(machine["blank"])
        )
    if not check_fields(machine["blank"], machine["alphabet"]):
        raise WrongBlankFieldError(
            "Blank value not in alphabet", set(machine["blank"])
        )


def check_transitions_fields(machine: dict):
    """Check if all transitions values are in states"""
    if not check_fields(machine["transitions"], machine["states"]):
        raise WrongTransitionsFieldsError(
            "Transitions fields not in states",
            set(machine["transitions"]) - set(machine["states"]),
        )


def check_initial_field(machine: dict):
    """Check if initial field value is in states"""
    if not check_fields([machine["initial"]], machine["states"]):
        raise WrongInitialFieldError(
            "Initial field value not in states", machine["initial"]
        )


def check_finals_field(machine: dict):
    """Check if finals values are in states"""
    if not check_fields(machine["finals"], machine["states"]):
        raise WrongFinalsFieldError(
            "Finals field values not in states",
            set(machine["finals"]) - set(machine["states"]),
        )


def check_transition_definition(machine: dict):
    """Check if all definitions are well formated"""
    required_fields = ["read", "to_state", "write", "action"]
    if not all(value for value in machine["transitions"].values()):
        raise TransitionsDefinitionFieldError(
            "Missing transition definition field",
            set(
                key
                for key, value in machine["transitions"].items()
                if not value
            ),
        )
    for transition_list in machine["transitions"].values():
        for item in transition_list:
            if not isinstance(item, dict):
                raise TransitionsDefinitionFieldError(
                    "Missing transition definition field", set(item)
                )
            if not check_fields(required_fields, item.keys()):
                raise TransitionsDefinitionFieldError(
                    "Transition definition error",
                    set(required_fields) - set(item.keys()),
                )


def check_transition_values(machine: dict):
    """Check if all values in transitions are allowed"""
    for transition_name, transition_list in machine["transitions"].items():
        for item in transition_list:
            if item["read"] not in machine["alphabet"]:
                raise TransitionValueError(
                    f"Wrong transition value for {transition_name} read",
                    item["read"],
                )
            if item["to_state"] not in machine["states"]:
                raise TransitionValueError(
                    f"Wrong transition value for {transition_name} to_state",
                    item["to_state"],
                )
            if item["write"] not in machine["alphabet"]:
                raise TransitionValueError(
                    f"Wrong transition value for {transition_name} write",
                    item["write"],
                )
            if item["action"] not in ["RIGHT", "LEFT", "NONE"]:
                raise TransitionValueError(
                    f"Wrong transition value for {transition_name} action",
                    item["action"],
                )
