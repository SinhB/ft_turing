import sys
import json

def check_state(machine: object, current_state: str):
    if current_state == 'HALT':
        sys.exit()
    if current_state not in machine['states']:
        sys.exit(f"Sate {current_state} doesn't exist in machine states ({machine['states']})")
    if current_state not in machine['transitions'].keys():
        sys.exit(f"Sate {current_state} doesn't exist in machine transitions ({list(machine['transitions'].keys())})")

def update_tape(tape: str, head: str, write: str):
    return f"{tape[0:head]}{write}{tape[head+1:]}"

def perform_transition(machine: object, tape: list, head: int, current_state: str, transition: object):
    if len(transition) != 1:
        sys.exit(f"Expected 1 transition for state {current_state} with read {tape[head]}, got {len(transition)}")
    print(f"[{tape[0:head]}<{tape[head]}>{tape[head+1:]}]  |  ({current_state}, {tape[head]}) -> ({transition[0]['to_state']}, {transition[0]['write']}, {transition[0]['action']})")
    engine(machine, transition[0]['to_state'], update_tape(tape, head, transition[0]['write']), head + 1 if transition[0]['action'] == 'RIGHT' else head - 1)


def engine(machine: object, current_state: str, tape: list, head: int):
    if tape[head] not in machine['alphabet']:
        sys.exit(f"Value {tape[head]} is not in the alphabet")
    check_state(machine, current_state)
    perform_transition(machine, tape, head, current_state, list(filter(lambda transition: transition['read'] == tape[head], machine['transitions'][current_state])))


if __name__ == "__main__":
    with open('unary_sub.json', 'r') as f:
        machine = json.load(f)
    initial_input = sys.argv[2]
    if machine['blank'] in initial_input:
        sys.exit(f"Blank character '{machine['blank']}' can't be on the tape")
    engine(machine=machine, current_state=machine['initial'], tape=initial_input, head=0)