"""ft turing"""

import argparse
from json import JSONDecodeError, load as json_load
import itertools

<<<<<<< HEAD
from src.engine import engine, run_engine
from src.utils.error import ParsingError
from src.utils.health_check import checks
=======
from engine import engine
from run_engine import run_engine
from utils.error import ParsingError
from utils.health_check import checks
from utils.plot import plot_complexity
>>>>>>> bonus

def generate_strings(chars, len):
    return [''.join(x) for x in itertools.product(chars, repeat=len)]

def get_input():
    """
    Get arguments input
    """
    parser = argparse.ArgumentParser()

    parser.add_argument("jsonfile", dest="jsonfile", help="json description of the machine")
    parser.add_argument("input", dest="input", help="input of the machine", type=str)
    parser.add_argument("bonus", dest="bonus", action=argparse.BooleanOptionalAction, help="complexity bonus", type=bool, default=False)
    return parser.parse_args()

def bonus():
    files_path = {
        '0n1n': 'machines_json/0n1n.json',
        '02n': 'machines_json/02n.json',
        'palindrome': 'machines_json/palindrome.json',
        'unary_add': 'machines_json/unary_add.json'
    }
    max_complexity = {'0n1n': [0], '02n': [0], 'palindrome': [0], 'unary_add': [0]}
    for key in files_path:
        with open(files_path[key], encoding="utf-8") as machine_description:
            machine = json_load(machine_description)
        for i in range(1, 4):
            no_blank_alphabet = [x for x in machine['alphabet'] if x not in machine['blank']]
            inputs = generate_strings(no_blank_alphabet, i)
            complexity = []
            for single_input in inputs:
                try:
                    complexity.append(engine(
                        machine=machine,
                        current_state=machine["initial"],
                        tape=(single_input + "."),
                        head=0,
                        count=0,
                        silent=True
                    ))
                except:
                    pass
            if complexity:
                max_complexity[key].append(max(complexity))
            else:
                max_complexity[key].append(0)
    plot_complexity(max_complexity)

if __name__ == "__main__":
    args = get_input()
    if args.bonus:
        bonus()
    else:
        try:
            machine, input = checks(args)
            # x = {
            #     'machine': machine,
            #     'current_state': machine["initial"],
            #     'tape': (input + "."),
            #     'head': 0,
            #     'count': 0
            # }
            # run_engine(x)
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
