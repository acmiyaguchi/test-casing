# Diff the three files and print a table of results
import sys


def main(argv):
    if len(argv) != 4:
        print(f"USAGE: {argv[0]} ORIGINAL JAVA RUST")
        sys.exit(1)

    print("| original | java | rust |")
    print("|---|---|---|")

    with open(argv[1]) as f0, open(argv[2]) as f1, open(argv[3]) as f2:
        lines = zip(f0.readlines(), f1.readlines(), f2.readlines())
        for original, java, rust in lines:
            if java == rust:
                continue
            print(f"| {original.strip()} | {java.strip()} | {rust.strip()} |")


if __name__ == "__main__":
    main(sys.argv)
