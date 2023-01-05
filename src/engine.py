import sys

from termcolor import colored

from utils.error import InfiniteLoopError, NoSolutionError, NoTransitionError

sys.setrecursionlimit(10000)


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


def check_known_states(known_states, tape, head, current_state):
    if tape in known_states:
        if current_state in known_states[tape]:
            if tape[head] in known_states[tape][current_state]:
                if head in known_states[tape][current_state][tape[head]]:
                    raise InfiniteLoopError("Infinite loop detected")
                else:
                    known_states[tape][current_state][tape[head]].append(head)
            else:
                known_states[tape][current_state][tape[head]] = [head]
        else:
            known_states[tape][current_state] = {tape[head]: [head]}
    else:
        known_states[tape] = {current_state: {tape[head]: [head]}}
    return known_states


def perform_transition(
    machine: object,
    tape: list,
    head: int,
    current_state: str,
    transition: object,
    count: int,
    silent: bool,
    known_states: object,
):
    if len(transition) != 1:
        raise NoTransitionError(
            f"Expected 1 transition for state {current_state} with read {tape[head]}, got {len(transition)}"
        )
    if not silent:
        print_tape(tape, head, current_state, transition)

    return engine(
        machine,
        transition[0]["to_state"],
        update_tape(tape, head, transition[0]["write"]),
        get_action(head, transition[0]["action"]),
        count + 1,
        silent,
        check_known_states(known_states, tape, head, current_state),
    )


def engine(
    machine: object,
    current_state: str,
    tape: list,
    head: int,
    count: int,
    silent: bool = False,
    known_states: object = {},
):
    if current_state in machine["finals"]:
        return count
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
        count,
        silent,
        known_states,
    )
