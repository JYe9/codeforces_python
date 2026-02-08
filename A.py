#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Codeforces Problem A Template
"""

import sys

input = sys.stdin.readline

def solve():
    """
    Main solution function for problem A
    """
    try:
        line = input().split()
        if not line: return
        n = int(line[0])
        w = int(line[1])
    except ValueError:
        return

    
    removed_boards = n - (n // w)
    
    print(removed_boards)


def main():
    """
    Handle multiple test cases
    """
    try:
        t_str = input().strip()
        if not t_str: return
        t = int(t_str)  # number of test cases
        for _ in range(t):
            solve()
    except ValueError:
        pass

if __name__ == "__main__":
    main()