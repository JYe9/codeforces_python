#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Codeforces Problem D Template
"""

import sys
from collections import defaultdict

sys.setrecursionlimit(200000)
input = sys.stdin.readline

MOD = 998244353 

def solve():
    try:
        line1 = input().split()
        if not line1: return
        n, m = map(int, line1)
        
        a = list(map(int, input().split()))
        
        edges = []
        for _ in range(m):
            u, v = map(int, input().split())
            edges.append((u, v))
            
    except ValueError:
        return

    edges.sort(key=lambda x: (a[x[1]-1], a[x[0]-1]))
    
    dp = [defaultdict(int) for _ in range(n + 1)]
    
    total_ans = 0
    
    for u, v in edges:
        val_u = a[u-1]
        val_v = a[v-1]
        
        # 1. Base Path (u -> v)
        current_paths = 1
        
        # 2. Try to extend the path: ... -> t -> u -> v
        # We need t to satisfy: val_t + val_u = val_v
        # i.e. val_t = val_v - val_u
        target_prev_val = val_v - val_u
        
        if target_prev_val >= 1:
            if target_prev_val in dp[u]:
                count_extendable = dp[u][target_prev_val]
                current_paths = (current_paths + count_extendable) % MOD
        
        # 3. Add to total answer
        total_ans = (total_ans + current_paths) % MOD
        
        # 4. Update the book of v
        # The current path ends with v, and the previous value is val_u
        dp[v][val_u] = (dp[v][val_u] + current_paths) % MOD
        
    print(total_ans)


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