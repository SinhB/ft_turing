"""Encoding TM for UTM simulation

    paper : "http://people.cs.uchicago.edu/~simon/OLD/COURSES/CS311/UTM.pdf"
    <M,w>
    M = the description of some Turing Machine
    w = an input string for M

    U = Universal Turing Machine
    3 sections:
        - buffer
        - machine description
        - tape description
    A = {0, 1, X, Y, Z, B} (alphabet)
    Q = turing states
    buffer len = (r + s + 2) -> r = number or states, s = number of symbols in alphabet

    Turing program:
        BLANK_VALUE = 1
        a1 = 11
        a2 = 111
        ...
        an = 1(n) + 1

        LEFT = 1
        NONE = 11
        RIGHT = 111

        q0 = 1
        q1 = 11
        ...
        qn = 1(n) + 1
        halt = (1)n + 2
        
        separator = 0
        quintuplet separator = 00

        X represent first symbol
        Y and Z are tape markers
        B is an auxiliary symbol

        Example of pseudo turing program:

        X 00000 Y 101011101 000 Z 11010110

        BUFFER = X00000 (preceded by X)
        MACHINE DESCRIPTION = Y101011101000 (preceded by Y and followed by 000)
        TAPE DESCRIPTION = Z11010110 (preceded by Z)
"""


import argparse
from json import JSONDecodeError

from src.engine import engine
from error import ParsingError
from health_check import checks



def get_input():
    """
    Get arguments input
    """
    parser = argparse.ArgumentParser()

    parser.add_argument("jsonfile", help="json description of the machine")
    parser.add_argument("input", help="input of the machine", type=str)
    return parser.parse_args()

def encode_states_or_alphabet(machine_list):
    """
    Encode states or alphabet
    """
    encoded_dict = {}
    for counter, item in enumerate(machine_list, 1):
        encoded_dict[item] = "1" * counter
    return encoded_dict

def encode_transitions(machine_transitions, encoded_states, encoded_aphabet):
    """
    Encode transitions
    """
    encoded_transitions_list = []
    def encode_transition(name, transition):
        for item in transition:
            direction = "1" if item["action"] == "LEFT" else "111"
            read = encoded_aphabet[item["read"]]
            to_state = encoded_states[item["to_state"]]
            write = encoded_aphabet[item["write"]]
            encoded_transition= f"{name}0{read}0{to_state}0{write}0{direction}"
            encoded_transitions_list.append(encoded_transition)
    for name, transition in machine_transitions.items():
        encode_transition(encoded_states[name], transition)
    return encoded_transitions_list

def encode_input(tm_input, alphabet):
    """
    Encode the input
    """
    encoded_input_list = []
    for symbol in tm_input:
        encoded_input_list.append(alphabet[symbol])
    return "0".join(encoded_input_list)

def encode(machine: dict, tm_input):
    """
    Encode machine
    """
    states = encode_states_or_alphabet(machine["states"])
    alphabet = encode_states_or_alphabet(machine["alphabet"])

    #Create buffer part
    buffer_size = len(machine["states"]) + len(machine["alphabet"]) + 2
    buffer = f"X{'0' * buffer_size}"

    #Create machine description part
    transitions = encode_transitions(machine["transitions"], states, alphabet)
    turing_number = "00".join(transitions)
    
    #Create tape description part
    encoded_input = encode_input(tm_input + ".", alphabet)

    #Create whole input
    utm_input = f"{buffer}QY{turing_number}000Z{encoded_input}"
    return utm_input


if __name__ == "__main__":
    args = get_input()
    try:
        machine, tm_input = checks(args)
        utm_input = encode(machine, tm_input)
        print(utm_input)
    except JSONDecodeError as e:
        print("JSON format error")
        print(e)
    except ParsingError as e:
        print(e)
