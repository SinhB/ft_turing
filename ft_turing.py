"""ft turing"""

import argparse
from json import JSONDecodeError

from core import run_machine
from error import ParsingError

def get_input():
    """
    Get arguments input
    """
    parser = argparse.ArgumentParser()

    parser.add_argument("jsonfile", help="json description of the machine")
    # ,
    #                     type=argparse.FileType("r"))
    parser.add_argument("input", help="input of the machine", type=str)
    args = parser.parse_args()
    return args

if __name__ == "__main__":
    arguments = get_input()
    try:
        run_machine(arguments)
    except JSONDecodeError as e:
        print("JSON format error")
        print(e)
    except ParsingError as e:
        print(e)