import argparse
import json


def get_input():
    """
    Get arguments input
    """
    parser = argparse.ArgumentParser()

    parser.add_argument("jsonfile", help="Decode keys of the alphabet machine")
    parser.add_argument(
        "utm_output", help="output of the utm machine", type=str
    )
    return parser.parse_args()


def get_args(arguments):
    """
    Get utm output and decoding keys as a dict
    """
    with open(arguments.jsonfile) as decode_json_keys:
        decode_keys = json.load(decode_json_keys)
    return decode_keys, arguments.utm_output


def decode_output(decode_keys, utm_output):
    """
    Decode output string from keys
    """
    output_tokens = utm_output.strip("0").split("0")
    decoded_output = ""
    for token in output_tokens:
        decoded_output += decode_keys[token]
    print(decoded_output)


if __name__ == "__main__":
    args = get_input()
    try:
        decode_keys, utm_output = get_args(args)
        decode_output(decode_keys, utm_output)
    except json.JSONDecodeError as e:
        print("JSON format error")
        print(e)
    except KeyError as e:
        print(f"Key does not exist: {e}")
    except FileNotFoundError as e:
        print(f"The following file does not exist: {e.filename}")
