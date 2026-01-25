#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Codeforces Problem E: Product Queries
"""

import sys
from collections import deque

def solve():
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
        
        unique_elements = sorted(list(set(a)))
        
        has_one = (unique_elements[0] == 1)
        
        if has_one:
            multipliers = unique_elements[1:]
        else:
            multipliers = unique_elements
            
        dist = [-1] * (n + 1)
        queue = deque()
        
        for x in multipliers:
            if x <= n:
                dist[x] = 1
                queue.append(x)
        
        if has_one:
            dist[1] = 1
            
        while queue:
            u = queue.popleft()
            
            for v in multipliers:
                next_val = u * v
                
                if next_val > n:
                    break
                
                if dist[next_val] == -1:
                    dist[next_val] = dist[u] + 1
                    queue.append(next_val)
        
        print(*(dist[1:]))

if __name__ == "__main__":
    solve()