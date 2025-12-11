#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Codeforces Problem B Template
"""

import sys

sys.setrecursionlimit(2000)

def solve():
    try:
        line1 = sys.stdin.readline()
        if not line1: return
        n = int(line1.strip())
        
        line2 = sys.stdin.readline()
        if not line2: return
        s = line2.strip()
    except ValueError:
        return

    if '0' not in s:
        print(0)
        return

    doubled_s = s + s
    zero_segments = doubled_s.split('1')

    max_zeros = 0
    for segment in zero_segments:
        max_zeros = max(max_zeros, len(segment))

    print(max_zeros)


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