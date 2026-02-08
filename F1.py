#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Codeforces Problem F Template
"""

import sys

sys.setrecursionlimit(200000)

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    iterator = iter(input_data)
    
    try:
        num_test_cases = int(next(iterator))
    except StopIteration:
        return

    MOD = 10**9 + 7
    results = []

    for _ in range(num_test_cases):
        n = int(next(iterator))
        k = int(next(iterator))
        
        adj = [[] for _ in range(n + 1)]
        for _ in range(n - 1):
            u = int(next(iterator))
            v = int(next(iterator))
            adj[u].append(v)
            adj[v].append(u)
        
        a = [int(next(iterator)) for _ in range(n)]
        b = [int(next(iterator)) for _ in range(k)]
        b_set = set(b)
        
        basis = []
        for val in b:
            temp = val
            for b_val in basis:
                temp = min(temp, temp ^ b_val)
            if temp > 0:
                basis.append(temp)
                basis.sort(reverse=True)
        
        sz = len(basis)
        
        val_map = {}   # mask -> value
        mask_map = {}  # value -> mask
        
        for m in range(1 << sz):
            cur_val = 0
            for i in range(sz):
                if (m >> i) & 1:
                    cur_val ^= basis[i]
            val_map[m] = cur_val
            mask_map[cur_val] = m
            
        parent = [0] * (n + 1)
        order = []
        stack = [1]
        
        visited = [False] * (n + 1)
        visited[1] = True
        
        topo_order = []
        q = [1]
        while q:
            u = q.pop()
            topo_order.append(u)
            for v in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    parent[v] = u
                    q.append(v)
        
        reverse_order = topo_order[::-1]
        
        S = [0] * (n + 1)
        dp = [[0] * (1 << sz) for _ in range(n + 1)]
        
        A_vals = [0] + a
        
        for u in reverse_order:
            S[u] = A_vals[u]
            dp[u][0] = 1
            
            for v in adj[u]:
                if v == parent[u]:
                    continue
                
                S[u] ^= S[v]
                
                new_dp = [0] * (1 << sz)
                
                s_v_mask = mask_map.get(S[v], -1)
                ways_cut = 0
                
                if s_v_mask != -1:
                    for m_v in range(1 << sz):
                        if dp[v][m_v] > 0:
                            comp_val = val_map[s_v_mask ^ m_v]
                            if comp_val in b_set:
                                ways_cut = (ways_cut + dp[v][m_v]) % MOD
                
                for m_u in range(1 << sz):
                    if dp[u][m_u] == 0:
                        continue
                        
                    current_ways = dp[u][m_u]
                    
                    if ways_cut > 0:
                        target_mask = m_u ^ s_v_mask
                        new_dp[target_mask] = (new_dp[target_mask] + current_ways * ways_cut) % MOD
                    
                    for m_v in range(1 << sz):
                        if dp[v][m_v] == 0:
                            continue
                        target_mask = m_u ^ m_v
                        new_dp[target_mask] = (new_dp[target_mask] + current_ways * dp[v][m_v]) % MOD
                
                dp[u] = new_dp

        ans = 0
        s_root_mask = mask_map.get(S[1], -1)
        
        if s_root_mask != -1:
            for m in range(1 << sz):
                if dp[1][m] > 0:
                    final_val = val_map[s_root_mask ^ m]
                    if final_val in b_set:
                        ans = (ans + dp[1][m]) % MOD
                        
        results.append(str(ans))

    print('\n'.join(results))

if __name__ == '__main__':
    solve()