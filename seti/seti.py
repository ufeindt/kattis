#! /usr/bin/python3

import sys


def decode_transcript(transcript):
    """Convert transcribed string to integers"""
    signal = []
    for character in transcript:
        if character == "*":
            signal.append(0)
        else:
            # ASCII for 'a' is 97
            signal.append(ord(character) - 96)

    return signal


def memoize(f):
    """Memoization for modular_multiplication_inverse()"""
    memo = {}

    def helper(a, p):
        if (a, p) not in memo:
            val = f(a, p)
            memo[(a, p)] = val
            memo[(val, p)] = a
        return memo[(a, p)]
    return helper


@memoize
def modular_multiplication_inverse(a, p):
    """Find inverse a_inv of multiplication by a on the residual field Z/pZ 
    where p is prime
    """
    a = a % p
    if a == 0:
        raise ValueError("'a' cannot be multiple of 'p'")

    # First handle special cases that are easy
    if a in [1, p-1]:
        return a
    elif a == 2:
        return int((p+1) / 2)

    # (a*a_inv) % p == 1 => There exists an integer k >= 0 such that
    # (k*p+1) / a = a_inv
    # Also k > 0 iff a > 1.
    k = 0
    while (k*p+1) % a != 0:
        k += 1
        if k > p:
            raise ValueError('Something went wrong. Are you sure p is prime?')
    return int((k*p+1) / a)


def backward_transcription(f_k, p):
    """Convert transcribed string back to original numbers using gaussian elimination
    """
    n = len(f_k)

    # Construct the matrix used in the transcription as list of rows
    matrix = [[(k**i) % p for i in range(n)] for k in range(1, n+1)]

    # Forward substitution
    for i in range(n):
        # Normalize current row
        inverse = modular_multiplication_inverse(matrix[i][i], p)
        matrix[i][i] = 1
        f_k[i] = (f_k[i] * inverse) % p
        for k in range(i+1, n):
            matrix[i][k] = (matrix[i][k] * inverse) % p

        # Subtract from rows below
        for j in range(i+1, n):
            f_k[j] = (f_k[j] - matrix[j][i] * f_k[i]) % p
            for k in range(i+1, n): 
                matrix[j][k] = (matrix[j][k] - matrix[j][i] * matrix[i][k]) % p
            matrix[j][i] = 0    

    # Backward substitution
    for i in range(n-1, -1, -1):
        # Subtract from rows above but no need to keep track of the matrix changes 
        # because they won't affect subsequent steps
        for j in range(i-1, -1, -1):
            f_k[j] = (f_k[j] - matrix[j][i] * f_k[i]) % p

    return f_k

def main():
    for line in sys.stdin:
        line = line.strip().split()
        if len(line) == 2:
            p, transcript = line
            p = int(p)
            result = backward_transcription(decode_transcript(transcript), p)
            print(' '.join([str(a) for a in result]))


if __name__ == "__main__":
    main()
