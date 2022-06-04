"""Runs the toast passed in by name, as specified in `toasts.json`."""

from argparse import ArgumentParser
from json import load
from random import choice

from plyer import notification


def main() -> None:
    """Parse arguments and show correct toast"""
    with open("toasts.json", "r") as toast_file:
        toasts: dict = load(toast_file)

    parser = ArgumentParser()
    parser.add_argument(
        "toast",
        choices=toasts.keys(),
        help="Toast configuration to send",
        type=str
    )

    config = toasts[parser.parse_args().toast]

    notification.notify(
        title=choice(config['title']),
        message=choice(config['message'])
    )


if __name__ == "__main__":
    main()
