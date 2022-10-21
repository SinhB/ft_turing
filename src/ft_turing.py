"""ft turing"""

import argparse
from json import JSONDecodeError
import itertools

from src.engine import engine
from src.utils.error import ParsingError
from src.utils.health_check import checks

def generate_strings(chars, len):
    return [''.join(x) for x in itertools.product(chars, repeat=len)]

def get_input():
    """
    Get arguments input
    """
    parser = argparse.ArgumentParser()

    parser.add_argument("jsonfile", help="json description of the machine")
    parser.add_argument("input", help="input of the machine", type=str)
    parser.add_argument("bonus", help="complexity bonus", type=bool, default=False)
    return parser.parse_args()


if __name__ == "__main__":
    args = get_input()
    try:
        machine, input = checks(args)
        if args.bonus:
            print(machine)
            max_complexity = []
            for i in range(0, 5):
                inputs = generate_strings(machine, i)
                complexity = []
                for single_input in inputs:
                    complexity.append(engine(
                        machine=machine,
                        current_state=machine["initial"],
                        tape=(single_input + "."),
                        # tape=input,
                        head=0,
                        count=0
                    ))
            max_complexity.append(max(complexity))
        else:
            engine(
                machine=machine,
                current_state=machine["initial"],
                tape=(input + "."),
                # tape=input,
                head=0,
            )
    except JSONDecodeError as e:
        print("JSON format error")
        print(e)
    except ParsingError as e:
        print(e)
