#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Codeforces Problem A
"""

def solve():
    """
    Main solution function for problem A
    """
    try:
        line = input().split()
        if not line: return
        n = int(line[0])
    except EOFError:
        return

    
    left = (n + 1) // 2
    right = left + 1
    
    result = []
    
    for i in range(n):
        if i % 2 == 0:
            result.append(left)
            left -= 1
        else:
            result.append(right)
            right += 1
            
    print(*result)


def main():
    """
    Handle multiple test cases
    """
    try:
        t_str = input().strip()
        if not t_str: return
        t = int(t_str)
        
        for _ in range(t):
            solve()
            
    except (EOFError, ValueError):
        pass

if __name__ == "__main__":
    main()