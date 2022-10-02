"""ft turing"""

import argparse
from json import JSONDecodeError
from engine import engine

from error import ParsingError
from health_check import checks

def get_input():
    """
    Get arguments input
    """
    parser = argparse.ArgumentParser()

    parser.add_argument("jsonfile", help="json description of the machine")
    parser.add_argument("input", help="input of the machine", type=str)
    args = parser.parse_args()
    return args

if __name__ == "__main__":
    args = get_input()
    try:
        machine, input = checks(args)
        engine(machine=machine, current_state=machine['initial'], tape=input, head=0)
    except JSONDecodeError as e:
        print("JSON format error")
        print(e)
    except ParsingError as e:
        print(e)