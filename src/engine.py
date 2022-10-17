import sys
from termcolor import colored


def update_tape(tape: str, head: str, write: str):
    return f"{tape[0:head]}{write}{tape[head+1:]}"

def print_tape(tape:str, head: str, current_state: str, transition: object):
    print(
        f"[{tape[0:head]}{colored('<'+tape[head]+'>', 'green')}{tape[head+1:]}]"
        f"  |  ({current_state}, {tape[head]}) ->"
        f" ({transition[0]['to_state']},"
        f" {transition[0]['write']}, {transition[0]['action']})"
    )

def perform_transition(
    machine: object,
    tape: list,
    head: int,
    current_state: str,
    transition: object,
):
    if len(transition) != 1:
        sys.exit(
            f"Expected 1 transition for state {current_state}"
            f" with read {tape[head]}, got {len(transition)}"
        )
    print_tape(tape, head, current_state, transition)
    engine(
        machine,
        transition[0]["to_state"],
        update_tape(tape, head, transition[0]["write"]),
        head + 1 if transition[0]["action"] == "RIGHT" else head - 1,
    )


def engine(machine: object, current_state: str, tape: list, head: int):
    if current_state in machine["finals"]:
        sys.exit(
            # f"[{tape[0:head]}<{tape[head]}>{tape[head+1:]}]"
            # f"  |  ({current_state}, {tape[head]})"
        )
    if head == len(tape) or head < 0:
        sys.exit("no solution")
    perform_transition(
        machine,
        tape,
        head,
        current_state,
        list(
            filter(
                lambda transition: transition["read"] == tape[head],
                machine["transitions"][current_state],
            )
        ),
    )