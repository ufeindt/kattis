#! /usr/bin/python3

"""
Notes:
- The power must be a divisor of the length 
"""

import sys


def get_divisors(n):
    """Get list of divisors of n > 0"""
    divisors = [1, n]
    i = 2
    while i**2 <= n:
        if n % i == 0:
            divisors.extend([i, n // i])
        i += 1

    return sorted(divisors)

def is_valid_string_power(n, string):
    """Check if the string could be a concatenation of n identical strings"""    
    length = len(string)
    base = string[:length//n]
    valid_power = True
    for k in range(1, n):
        if string[k*(length//n):(k+1)*(length//n)] != base:
            valid_power = False
            break
    if valid_power:               
        return True


def find_power(string):
    divisors = get_divisors(len(string))

    # start with largest divisor
    for n in divisors[::-1]:
        if is_valid_string_power(n, string):
            return n


def main():
    for line in sys.stdin:
        string = line.strip()
        if string == '.':
            sys.exit(0)
        print(find_power(string))


if __name__ == "__main__":
    main()