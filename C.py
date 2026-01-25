#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Codeforces Problem C: Replace and Sum
"""

import sys

sys.setrecursionlimit(2000)

def solve():
    """
    Main solution function for problem C
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

    results = []
    
    for _ in range(t):
        n = next_int()
        q = next_int()
        
        a = [next_int() for _ in range(n)]
        b = [next_int() for _ in range(n)]
        
        c = [0] * n
        for i in range(n):
            c[i] = a[i] if a[i] > b[i] else b[i]
        
        suffix_max = [0] * n
        current_max = 0
        
        for i in range(n - 1, -1, -1):
            if c[i] > current_max:
                current_max = c[i]
            suffix_max[i] = current_max
            
        prefix_sum = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i+1] = prefix_sum[i] + suffix_max[i]
            
        query_results = []
        for _ in range(q):
            l = next_int()
            r = next_int()
            
            current_ans = prefix_sum[r] - prefix_sum[l-1]
            query_results.append(str(current_ans))
            
        results.append(" ".join(query_results))

    print("\n".join(results))

if __name__ == "__main__":
    solve()