#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Codeforces Problem B Template
"""

import sys

def solve():
    """
    Main solution logic
    """
    try:
        line1 = sys.stdin.read().split()
    except Exception:
        return

    if not line1:
        return

    iterator = iter(line1)
    
    try:
        t = int(next(iterator))
    except StopIteration:
        return

    output = []

    for _ in range(t):
        n = int(next(iterator))
        s = next(iterator)

        indices = [i for i, char in enumerate(s) if char == '1']
        
        if not indices:
            ans = (n - 1) // 3 + 1
            output.append(str(ans))
            continue

        added_students = 0
        
        k_left = indices[0]
        added_students += (k_left + 1) // 3
        
        k_right = n - 1 - indices[-1]
        added_students += (k_right + 1) // 3
        
        for i in range(len(indices) - 1):
            gap = indices[i+1] - indices[i] - 1
            added_students += gap // 3
            
        total_students = len(indices) + added_students
        output.append(str(total_students))

    print('\n'.join(output))

if __name__ == "__main__":
    solve()