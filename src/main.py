#!/usr/bin/env python3
import fileinput
import re
import string

WORD_BOUND_PAT = re.compile(
    r"""
    \b                                  # standard word boundary
    |(?<=[a-z])(?=[A-Z])                # aA -> a|A boundary
    |(?<=[A-Z])(?=[A-Z][a-z])        # AAAa -> AA|Aa boundary
    """,
    re.VERBOSE,
)


def snake_case(line: str) -> str:
    # replace non-alphanumeric characters with spaces
    subbed = re.sub(r"[^\w]|_", " ", line)
    words = WORD_BOUND_PAT.split(subbed)
    # filter space between words and snake_case
    return "_".join([w.lower() for w in words if w.strip()])


def main():
    for line in fileinput.input():
        print(snake_case(line.strip()))


if __name__ == "__main__":
    main()
