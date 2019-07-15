#!/usr/bin/env python3
import fileinput
import re

# Search for all camelCase situations in reverse with arbitrary lookaheads.
REV_WORD_BOUND_PAT = re.compile(
    r"""
    \b                                  # standard word boundary
    |(?<=[A-Z])(?=[a-z])                # aA -> a|A boundary
    |(?<=[a-z][A-Z])(?=[A-Z])           # AAa -> A|Aa boundary
    |(?<=[a-z][A-Z])(?=\d*[A-Z])        # A7Aa -> A7|Aa boundary
    |(?<=[a-z][A-Z])(?=\d*[a-z])        # a7Aa -> a7|Aa boundary
    |(?<=[A-Z])(?=\d*[a-z])             # a7A -> a7|A boundary
    """,
    re.VERBOSE,
)


def snake_case(line: str) -> str:
    # replace non-alphanumeric characters with spaces in the reversed line
    subbed = re.sub(r"[^\w]|_", " ", line[::-1])

    # apply the regex on the reversed string
    words = REV_WORD_BOUND_PAT.split(subbed)

    # filter spaces between words and snake_case and reverse again
    return "_".join([w.lower() for w in words if w.strip()])[::-1]


def main():
    for line in fileinput.input():
        print(snake_case(line.strip()))


if __name__ == "__main__":
    main()
