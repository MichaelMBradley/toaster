# C:/Windows/py.exe
# Creates a random notification to remind me to look outside

from argparse import ArgumentParser
from random import randrange
from types import FunctionType
from typing import List

from win10toast import ToastNotifier


class Toast:
    def end_day() -> None:
        """Toast a reminder of things to do at the end of the day"""
        toast(
            title="End of day reminder",
            msg="Fill out timesheet, comment today's work on Jira."
        )


    def eye_saver() -> None:
        """Toast a reminder to look outside"""
        toast(
            title=random_item(
                [
                    "Save your eyes",
                    "Look outside",
                    "Touch grass",
                    "Eye strain reduction",
                    "Eye saver"
                    ]
                ),
            msg=random_item(
                [
                    "20-20-20",
                    "Every 20 minutes look at something 20 feet away for 20 seconds",
                    "Touch grass",
                    "Let's try to avoid needing glasses",
                    "Look outside",
                    "Eye suggest you look outside",
                    "Eye suggest you avoid eye strain",
                    "I care about eye care"
                    ]
                )
            )


def main() -> None:
    """Parse arguments, call toaster"""
    functions = [
        *filter(
            lambda attr: isinstance(vars(Toast)[attr], FunctionType),
            vars(Toast)
            )
        ]
    
    parser = ArgumentParser()
    parser.add_argument(
        "-t",
        choices=functions,
        help="Type of toast to send",
        required=True,
        type=str
        )
    
    exec(f"Toast.{vars(parser.parse_args())['t']}()")


def random_item(arr: List[str]) -> str:
    """Choose random string from list"""
    return arr[randrange(len(arr))]


def toast(title: str, msg: str) -> None:
    """Show toast with string and title"""
    ToastNotifier().show_toast(
        title=title,
        msg=msg,
        icon_path=None,
        duration=5,
        threaded=False
    )


if __name__ == "__main__":
    main()
