import json
from error import BlankInInput, InputCharError, MissingFieldError, TransitionsDefinitionFieldError, WrongBlankFieldError, WrongFinalsFieldError, WrongInitialFieldError, WrongTransitionsFieldsError

def print_pretty_json(json_dict):
    """Print beauty json"""
    print(json.dumps(json_dict, indent=4))

def checks(arguments):
    """Checks arguments"""
    return input_check(health_check(arguments.jsonfile), arguments.input)

def health_check(jsonfile: dict):
    """Perform health check of the machine description"""
    with open(jsonfile, encoding="utf-8") as machine_description:
        machine = json.load(machine_description)
        check_machine_fields(machine)
        check_blank_field(machine)
        check_transitions_fields(machine)
        check_initial_field(machine)
        check_finals_field(machine)
        check_transition_definition(machine)
    return machine

def input_check(machine: dict, input: str):
    """Check input format"""
    if any(char in input for char in machine["blank"]):
        raise BlankInInput("Blank char in input")
    if not check_fields(input, machine["alphabet"]):
        raise InputCharError("Wrong char in input")
    return machine, input

def check_fields(lookup, fields):
    """Return True if all item in lookup are in fields"""
    return all(field in fields for field in lookup)

def check_machine_fields(machine: dict):
    """Check if a required_fields are in the machine"""
    required_fields = ["name", "alphabet", "blank", "states", "initial", "finals", "transitions"]
    if not check_fields(required_fields, machine):
        raise MissingFieldError("Missing fields in machine description")

def check_blank_field(machine: dict):
    """Check if the blank field value is in the alphabet field"""
    if not check_fields(machine["blank"], machine["alphabet"]):
        raise WrongBlankFieldError("Blank field not in alphabet")

def check_transitions_fields(machine: dict):
    """Check if all transitions values are in states"""
    if not check_fields(machine["transitions"], machine["states"]):
        raise WrongTransitionsFieldsError("Transitions fields not in states")

def check_initial_field(machine: dict):
    """Check if initial field value is in states"""
    if not check_fields([machine["initial"]], machine["states"]):
        raise WrongInitialFieldError("Initial field value not in states")

def check_finals_field(machine: dict):
    """Check if finals values are in states"""
    if not check_fields(machine["finals"], machine["states"]):
        raise WrongFinalsFieldError("Finals field values not in states")

def check_transition_definition(machine: dict):
    """Check if all definitions are well formated"""
    required_fields = ["read", "to_state", "write", "action"]
    if not any(value for value in machine["transitions"].values()):
        raise TransitionsDefinitionFieldError("Missing transition definition field")        
    for transition_list in machine["transitions"].values():
        for item in transition_list:
            if not isinstance(item, dict):
                raise TransitionsDefinitionFieldError("Missing transition definition field")
            if not check_fields(required_fields, item.keys()):
                raise TransitionsDefinitionFieldError("Transition definition error")