#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Codeforces Problem B: Reverse a Permutation
"""

def solve():
    """
    Main solution function for problem B
    """
    n = int(input())
    
    p = list(map(int, input().split()))
    
    target = n 
    
    for i in range(n):
        if p[i] == target:
            target -= 1
            continue
        
        target_index = p.index(target)
        
        segment = p[i : target_index + 1]
        p[i : target_index + 1] = segment[::-1]
        
        break
    
    print(*p)


def main():
    """
    Handle multiple test cases
    """
    # Read number of test cases
    input_str = input().strip()
    if not input_str:
        return
    t = int(input_str)
    
    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()