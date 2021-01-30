#! /usr/bin/python3

import sys


def rotate(rows):
    # Determine number of columns and pad the rows
    n_columns = max([len(r) for r in rows])
    padded = [r + ' '*(n_columns - len(r)) for r in rows]
    # print([len(r) for r in padded])

    # First rotate the columns to rows (invert n-th columns and reverse it to
    # make n-th row). Then replace '-' with '|' (using a placeholder) and strip
    # trailing spaces.
    rotated = []
    for k in range(n_columns):
        new_row = ''.join([r[k] for r in padded])[::-1]
        new_row = new_row.replace('-', '0')
        new_row = new_row.replace('|', '-')
        new_row = new_row.replace('0', '|')
        new_row = new_row.rstrip()
        rotated.append(new_row)

    return rotated


def main():
    n_rows = 0
    for i, line in enumerate(sys.stdin):
        if n_rows == 0:
            n_rows = int(line.strip())
            rows = []
            if n_rows == 0:
                return
            elif i != 0:
                print()
        else:
            rows.append(line.rstrip())
            n_rows -= 1
            if n_rows == 0:
                rows = rotate(rows)
                for row in rows:
                    print(row)


if __name__ == '__main__':
    main()
