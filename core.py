import json
from itertools import repeat

from error import ParsingError

def print_pretty_json(json_dict):
    """Print beauty json"""
    print(json.dumps(json_dict, indent=4))

def run_machine(arguments):
    """Run machine"""
    machine = health_check(arguments.jsonfile)
    print_pretty_json(machine["transitions"])
    # print_pretty_json(machine)

def check_machine_fields(machine: dict):
    """Check if a key exist in the dict"""
    required_fields = ["name", "alphabet", "blank", "states", "initial", "finals", "transitions"]
    missing_fields = list(map(lambda keys, dict: keys in dict, required_fields, repeat(machine)))
    if all(missing_fields):
        return machine
    raise ParsingError("Missing fields in machine description")

def health_check(machine_description):
    """Perform health check of the machine description"""
    machine = json.load(open(machine_description, encoding="utf-8"))
    return check_machine_fields(machine)
    
