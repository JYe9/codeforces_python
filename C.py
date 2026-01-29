#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Codeforces Problem C Template
"""

import sys

sys.setrecursionlimit(2000)

def solve():
    """
    Main solution function for problem C
    """
    pass 

def run_logic():
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    iterator = iter(input_data)
    
    try:
        t = int(next(iterator))
    except StopIteration:
        return

    output = []

    for _ in range(t):
        n = int(next(iterator))
        a = []
        for _ in range(n):
            a.append(int(next(iterator)))

        b = sorted(a)

        if a == b:
            output.append("-1")
            continue

        min_val = b[0]
        max_val = b[-1]

        low = 1
        high = 10**9
        ans = 0

        while low <= high:
            mid = (low + high) // 2
            
            possible = True
            
            for i in range(n):
                can_move = False
                if abs(a[i] - min_val) >= mid:
                    can_move = True
                elif abs(a[i] - max_val) >= mid:
                    can_move = True
                
                if not can_move:
                    if a[i] != b[i]:
                        possible = False
                        break
            
            if possible:
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        
        output.append(str(ans))

    print('\n'.join(output))

def main():
    """
    Handle multiple test cases
    """
    run_logic()

if __name__ == "__main__":
    main()