"""ft turing"""

import argparse
import itertools
from json import JSONDecodeError
from json import load as json_load

from engine import engine
from universal_engine import run_engine
from utils.error import MachineError, ParsingError
from utils.health_check import checks
from utils.plot import plot_complexity


def generate_strings(chars, len):
    return ["".join(x) for x in itertools.product(chars, repeat=len)]


def get_input():
    """
    Get arguments input
    """
    parser = argparse.ArgumentParser()

    parser.add_argument("jsonfile", help="json description of the machine")
    parser.add_argument("input", help="input of the machine", type=str)
    parser.add_argument(
        "--universal",
        dest="universal",
        action=argparse.BooleanOptionalAction,
        help="Used to compute universal machine",
        type=bool,
        default=False,
    )
    return parser.parse_args()


def bonus():
    files_path = {
        "0n1n": "machines_json/0n1n.json",
        "02n": "machines_json/02n.json",
        "palindrome": "machines_json/palindrome.json",
        "unary_add": "machines_json/unary_add.json",
    }
    max_complexity = {
        "0n1n": [0],
        "02n": [0],
        "palindrome": [0],
        "unary_add": [0],
    }
    for key in files_path:
        with open(files_path[key], encoding="utf-8") as machine_description:
            machine = json_load(machine_description)
        for i in range(1, 10):
            no_blank_alphabet = [
                x for x in machine["alphabet"] if x not in machine["blank"]
            ]
            inputs = generate_strings(no_blank_alphabet, i)
            complexity = []
            for single_input in inputs:
                try:
                    complexity.append(
                        engine(
                            machine=machine,
                            current_state=machine["initial"],
                            tape=(single_input + "."),
                            head=0,
                            count=0,
                            silent=True,
                        )
                    )
                except Exception:
                    pass
            if complexity:
                max_complexity[key].append(max(complexity))
            else:
                max_complexity[key].append(0)
    plot_complexity(max_complexity)


if __name__ == "__main__":
    args = get_input()
    # bonus()
    # import sys
    # sys.exit()
    try:
        machine, tape = checks(args)
        if args.universal:
            x = {
                "machine": machine,
                "current_state": machine["initial"],
                "tape": (tape + "."),
                "head": 0,
            }
            run_engine(x)
        else:
            engine(
                machine=machine,
                current_state=machine["initial"],
                tape=(tape + "."),
                head=0,
                count=0,
            )
    except JSONDecodeError as e:
        print("JSON format error")
        print(e)
    except ParsingError as e:
        print(e)
    except MachineError as e:
        print(f"Error : {e}")
    except RecursionError:
        print("Maximum recursion exceeded, use --universal argument")
