#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Codeforces Problem A1 Template
"""

import sys

def solve():
    """
    Main solution function for problem A1
    """
    n = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))
    
    stack = []
    
    for i in range(n - 1, -1, -1):
        x = a[i]
        
        while stack and stack[-1] == x + 1:
            stack.pop()
            
        stack.append(x)
        
    result = len(stack)
    
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