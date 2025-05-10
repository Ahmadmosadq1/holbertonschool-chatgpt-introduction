#!/usr/bin/env python3
"""
factorial_recursive.py

Compute the factorial of a non-negative integer using a recursive function.

Usage:
    ./factorial_recursive.py <non-negative integer>

Example:
    $ ./factorial_recursive.py 4
    24
"""

import sys

def factorial(n):
    """
    Recursively compute n! (n factorial).

    Parameters:
        n (int): A non-negative integer

    Returns:
        int: The factorial of n (i.e., 1 * 2 * … * n)

    Raises:
        ValueError: If n is negative
    """
    if n < 0:
        # We don’t define factorials for negative inputs
        raise ValueError("Factorial is not defined for negative numbers.")
    if n == 0:
        # Base case: 0! is defined as 1
        return 1
    # Recursive case: n! = n * (n-1)!
    return n * factorial(n - 1)

def main():
    """Parse command-line arguments and print the computed factorial."""
    # Expect exactly one argument (besides the script name)
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <non-negative integer>", file=sys.stderr)
        sys.exit(1)

    # Convert to integer and handle any errors
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("Error: argument must be an integer.", file=sys.stderr)
        sys.exit(1)

    # Compute and print the result (or report negative inputs)
    try:
        result = factorial(n)
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

    print(result)

if __name__ == "__main__":
    main()

