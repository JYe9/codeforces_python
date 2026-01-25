#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Codeforces Problem D: Monster Game
"""

import sys

sys.setrecursionlimit(2000)

def solve():
    """
    Main solution function for problem D
    """
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    iterator = iter(input_data)
    
    def next_int():
        return int(next(iterator))

    try:
        t = next_int()
    except StopIteration:
        return

    for _ in range(t):
        n = next_int()
        
        a = [next_int() for _ in range(n)]
        b = [next_int() for _ in range(n)]
        
        a.sort(reverse=True)
        
        prefix_b = []
        current_sum = 0
        for val in b:
            current_sum += val
            prefix_b.append(current_sum)
            
        max_score = 0
        
        for i in range(n):
            swords_needed = prefix_b[i]
            
            if swords_needed > n:
                break
            
            difficulty_x = a[swords_needed - 1]
            
            current_score = difficulty_x * (i + 1)
            
            if current_score > max_score:
                max_score = current_score
                
        print(max_score)

if __name__ == "__main__":
    solve()