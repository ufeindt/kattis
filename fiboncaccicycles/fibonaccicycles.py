#! /usr/bin/python3

import sys

def main():
    for i, line in enumerate(sys.stdin):
        if i == 0:
            continue

        k = int(line.strip())

        fibonacci = [1, 1]
        while True:
            new = (fibonacci[-1] + fibonacci[-2]) % k
            if new not in fibonacci[2:]:
                fibonacci.append(new)
            else:
                print(fibonacci[2:].index(new)+2)
                break

if __name__ == "__main__":
    main()