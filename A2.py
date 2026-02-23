#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Codeforces Problem A2 Template
"""

import sys

def solve():
    n = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))
    
    stack = []
    L = [0] * (n + 1)
    
    for i in range(n, 0, -1):
        x = a[i - 1]
        
        while stack and a[stack[-1] - 1] == x + 1:
            popped_idx = stack.pop()
            L[popped_idx] = i
            
        stack.append(i)
       
    total_subarrays_len = n * (n + 1) * (n + 2) // 6
    
    total_pops = 0
    for j in range(1, n + 1):
        if L[j] > 0:
            total_pops += L[j] * (n - j + 1)
            
    result = total_subarrays_len - total_pops
    
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