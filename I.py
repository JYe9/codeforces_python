#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Codeforces Problem I Template
"""

def solve():
    """
    Main solution function for problem I
    """
    # Read input here
    n = int(input())
    
    # Your solution logic here
    result = n
    
    # Output result
    print(result)


def main():
    """
    Handle multiple test cases if needed
    """
    t = int(input())  # number of test cases
    for _ in range(t):
        solve()


if __name__ == "__main__":
    # For single test case, use: solve()
    # For multiple test cases, use: main()
    main()