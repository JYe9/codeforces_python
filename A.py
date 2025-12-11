#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Codeforces Problem A Template
"""
import sys

def solve():
    """
    Main solution logic
    """
    try:
        line = sys.stdin.readline()
        if not line:
            return
        n = int(line.strip())
        
        line2 = sys.stdin.readline()
        if not line2:
            return
        a = list(map(int, line2.split()))
    except ValueError:
        return

    if n == 0:
        print(0)
        return

    current_max = a[0]
    operations = 0
    
    for i in range(1, n):
        if a[i] < current_max:
            operations += 1
        else:
            current_max = a[i]
            
    print(operations)


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