#!/usr/bin/env python3
"""
Diff the three files and print a table of results.
"""
import sys
from contextlib import ExitStack


def main(argv):
    if len(argv) != 4:
        print(f"USAGE: {argv[0]} ORIGINAL JAVA RUST")
        sys.exit(1)

    filenames = argv[1:]

    print("original|java|rust")
    print("-|-|-")

    with ExitStack() as stack:
        files = [stack.enter_context(open(name)) for name in filenames]
        lines = zip(*[f.read().split() for f in files])
        for original, java, rust in lines:
            if java == rust:
                continue
            print(f"{original}|{java}|{rust}")


if __name__ == "__main__":
    main(sys.argv)
