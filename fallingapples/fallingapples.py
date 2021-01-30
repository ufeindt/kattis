#! /usr/bin/python3

import sys


def gravity(column):
    # First split by obstacles
    columns_split = column.split('#')

    # Now sort each piece ('.' will come before 'a')
    columns_sorted = [''.join(sorted(c)) for c in columns_split]

    return '#'.join(columns_sorted)


def main():
    columns = []
    for line in sys.stdin:
        if not columns:
            n_row = int(line.split()[1])
            columns = ['' for k in range(int(n_row))]
        else:
            for k, c in enumerate(line.strip()):
                columns[k] += c

    for k, column in enumerate(columns):
        columns[k] = gravity(column)

    for k in range(len(columns[0])):
        print(''.join([c[k] for c in columns]))


if __name__ == '__main__':
    main()
