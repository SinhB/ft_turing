"""ft turing"""

import argparse
from json import JSONDecodeError, load as json_load
import itertools
import math
import matplotlib.pyplot as plt

from engine import engine
from utils.error import ParsingError
from utils.health_check import checks

def generate_strings(chars, len):
    return [''.join(x) for x in itertools.product(chars, repeat=len)]

def get_input():
    """
    Get arguments input
    """
    parser = argparse.ArgumentParser()

    parser.add_argument("--jsonfile", dest="jsonfile", help="json description of the machine")
    parser.add_argument("--input", dest="input", help="input of the machine", type=str)
    parser.add_argument("--bonus", dest="bonus", action=argparse.BooleanOptionalAction, help="complexity bonus", type=bool, default=False)
    return parser.parse_args()

def plot_complexity(machine_result):
    linear_n = [0]
    O_logn = [0]
    O_n_logn = [0]
    O_n2 = [0]
    O_2n = [0]
    O_factorialn = [0]
    O_n_sqrtn = [0]
    O_sqrtn = [0]
    for n in range(1, 100):
        linear_n.append(n)
        O_logn.append(math.log(n))
        O_n_logn.append(n * math.log(n))
        O_n2.append(n ** 2)
        O_2n.append(2 ** n)
        O_factorialn.append(math.factorial(n))
        O_n_sqrtn.append(n * math.sqrt(n))
        O_sqrtn.append(math.sqrt(n))
    plt.plot(O_logn, color='red')
    plt.plot(linear_n, color='green')
    plt.plot(O_n_logn, color="purple")
    plt.plot(O_n2, color='cyan')
    plt.plot(O_2n, color='orange')
    plt.plot(O_factorialn, color='lightblue')
    plt.plot(O_n_sqrtn, color='yellow')
    plt.plot(O_sqrtn, color='magenta')

    plt.plot(machine_result, color='black')
    plt.legend(['O(logn)', 'O(n)', 'O(nlogn)', 'O(n**2)', 'O(2**n)', 'O(n!)', 'O(n_sqrtn)', 'O(sqrtn)', 'O(machine)'])
    plt.xlim([0, 100])
    plt.ylim([0, 1000])
    plt.grid()
    plt.show()

if __name__ == "__main__":
    args = get_input()
    plot_complexity([0, 3, 6, 9, 14, 19, 26, 33, 42, 51])
    import sys
    sys.exit()
    if args.bonus:
        with open(args.jsonfile, encoding="utf-8") as machine_description:
            machine = json_load(machine_description)
        max_complexity = [0]
        for i in range(1, 10):
            no_blank_alphabet = [x for x in machine['alphabet'] if x not in machine['blank']]
            inputs = generate_strings(no_blank_alphabet, i)
            complexity = []
            for single_input in inputs:
                # print(single_input)
                try:
                    complexity.append(engine(
                        machine=machine,
                        current_state=machine["initial"],
                        tape=(single_input + "."),
                        # tape=input,
                        head=0,
                        count=0
                    ))
                except:
                    pass
            if complexity:
                max_complexity.append(max(complexity))
            else:
                max_complexity.append(0)
        print(max_complexity)
    else:
        try:
            machine, input = checks(args)
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
