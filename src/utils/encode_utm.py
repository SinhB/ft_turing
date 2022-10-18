"""Encoding TM for UTM simulation"""

import argparse
import math
from json import JSONDecodeError

from click import argument

from src.engine import engine
from error import ParsingError
from health_check import checks


def get_input():
    """
    Get arguments input
    """
    parser = argparse.ArgumentParser()

    parser.add_argument("jsonfile", help="json description of the machine")
    return parser.parse_args()

def encode_states(machine_states):
    """
    Encode states
    """
    encoded_state_dict = {}
    size = int(math.log2(len(machine_states))) + 1
    for counter, state in enumerate(machine_states):
        state_type = "h" if state == "HALT" else "q"
        binary = str(bin(int(counter)))[2:].zfill(size)
        encoded_state_dict[state] = state_type + binary
    return encoded_state_dict

def encode_alphabet(machine_alphabet):
    """
    Encode states
    """
    encoded_alphabet_dict = {}
    size = int(math.log2(len(machine_alphabet)))
    for counter, char in enumerate(machine_alphabet):
        binary = str(bin(int(counter)))[2:].zfill(size)
        encoded_alphabet_dict[char] = "a" + binary
    return encoded_alphabet_dict

def encode(machine: dict):
    """
    Encode machine
    """
    states = encode_states(machine["states"])
    alphabet = encode_alphabet(machine["alphabet"])
    print(states)
    print(alphabet)


if __name__ == "__main__":
    args = get_input()
    try:
        machine = checks(args)
        encoded_machine = encode(machine)
        print(encoded_machine)
    except JSONDecodeError as e:
        print("JSON format error")
        print(e)
    except ParsingError as e:
        print(e)
