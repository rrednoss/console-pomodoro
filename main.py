import argparse
import sys
import time


def _create_cli():
    """
    Creates a command line interface (CLI) to control and start this script.
    """
    parser = argparse.ArgumentParser(
        description="The Pomodoro Technique is a time management method developed by Francesco Cirillo in the late 1980s. -Wikipedia",
    )
    parser.add_argument(
        "-c",
        "--cycles",
        default=4,
        help="set the number of doing/pause cycles",
        metavar="",
        type=int,
    )
    _start_pomodoro(parser.parse_args())


def _start_pomodoro(args):
    """
    Switches between doing and pause phases.

    At the end the terminal bell rings (only if the terminal application enabled the bell setting).
    """
    MINUTES_DOING = 25
    MINUTES_PAUSE = 5
    for _ in range(args.cycles):
        _exec_phase("DOING", MINUTES_DOING)
        _exec_phase("PAUSE", MINUTES_PAUSE)
    _ring_bell()


def _exec_phase(name, minutes):
    for i in range(minutes):
        print("{0}:".format(name), "{0} minutes to go".format(minutes - i))
        time.sleep(60)
    print()


def _ring_bell():
    sys.stdout.write("\a")  # ASCII sybmbol for 'bell'
    sys.stdout.flush()


if __name__ == "__main__":
    sys.exit(_create_cli())
