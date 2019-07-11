#!/usr/bin/env python3
import fileinput
import re

WORD_BOUNDARY_PATTERN = r"\b|(?<=[a-z])(?=[A-Z])|(?<=[A-Z0-9])(?=[A-Z][a-z])"


def snake_case(line):
    # Split a line based on the defined word boundaries. This will contain empty
    # spaces before and after the line. Underscores are considered as part of
    # word boundary in the predefined `\b`.
    words = re.split(WORD_BOUNDARY_PATTERN, line)
    cased = [w.strip("_").lower() for w in words if w]
    return "_".join(cased)


def main():
    for line in fileinput.input():
        print(snake_case(line.strip()))


if __name__ == "__main__":
    main()
