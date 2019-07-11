import fileinput


def snake_case(line):
    return line


def main():
    for line in fileinput.input():
        print(snake_case(line.strip()))


if __name__ == "__main__":
    main()
