#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Codeforces Problem B Template
"""

import sys

def solve():
    """
    Main solution function for problem B
    """
    line = sys.stdin.readline().split()
    if not line:
        return
    n = int(line[0])
    k = int(line[1])
    
    M = k - n
    
    if M < 0 or M > n - 1:
        print("NO")
        return
        
    print("YES")
    
    if M == 0:
        ans = []
        for i in range(1, n + 1):
            ans.extend([i, i])
        print(*(ans))
        return
        
    ans = []
    
    ans.extend([1, 2])
    
    for i in range(3, M + 2):
        ans.extend([i, i - 2])
        
    ans.extend([M, M + 1])
    
    for i in range(M + 2, n + 1):
        ans.extend([i, i])
        
    print(*(ans))


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