from termcolor import colored

from utils.error import NoSolutionError, NoTransitionError


def update_tape(tape: str, head: str, write: str):
    if tape[-1] != ".":
        return f"{tape[0:head]}{write}{tape[head+1:]}."
    return f"{tape[0:head]}{write}{tape[head+1:]}"


def print_tape(tape: str, head: str, current_state: str, transition: object):
    new_tape = f"{tape[0:head]}{colored(tape[head], 'green')}{tape[head+1:]}"
    if tape[head] != "X":
        new_tape = new_tape.replace("X", colored("X", "yellow"))
    if tape[head] != "Y":
        new_tape = new_tape.replace("Y", colored("Y", "red"))
    if tape[head] != "Q":
        new_tape = new_tape.replace("Q", colored("Q", "blue"))
    if tape[head] != "Z":
        new_tape = new_tape.replace("Z", colored("Z", "red"))
    print(
        f"[{new_tape}]"
        f"  |  ({current_state}, {tape[head]}) ->"
        f" ({transition[0]['to_state']},"
        f" {transition[0]['write']}, {transition[0]['action']})"
    )


def get_action(head, action):
    if action == "RIGHT":
        return head + 1
    if action == "LEFT":
        return head - 1
    return head


def perform_transition(
    machine: object,
    tape: list,
    head: int,
    current_state: str,
    transition: object,
):
    if len(transition) != 1:
        raise NoTransitionError(
            f"Expected 1 transition for state {current_state}"
            + f" with read {tape[head]}, got {len(transition)}"
        )
    print_tape(tape, head, current_state, transition)
    return {
        "machine": machine,
        "current_state": transition[0]["to_state"],
        "tape": update_tape(tape, head, transition[0]["write"]),
        "head": get_action(head, transition[0]["action"]),
    }


def engine(machine: object, current_state: str, tape: list, head: int):
    if current_state in machine["finals"]:
        return 0
    if head == len(tape) or head < 0:
        raise NoSolutionError("no solution")
    return perform_transition(
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


def run_engine(x: dict):
    while type(x) != int:
        x = engine(
            x["machine"],
            x["current_state"],
            x["tape"],
            x["head"],
        )
    return x
