#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Codeforces Problem F Template
"""

MOD = 10**9 + 7

def solve():
    n, k = map(int, input().split())
    
    adj = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)
    
    a = [0] + list(map(int, input().split()))
    b_set = set(map(int, input().split()))
    
    def dfs(u, parent):
        dp = [(a[u], 1)]
        
        for v in adj[u]:
            if v == parent:
                continue
            
            child_dp = dfs(v, u)
            new_dp_dict = {}
            
            for xor_u, cnt_u in dp:
                for xor_v, cnt_v in child_dp:
                    if xor_v in b_set:
                        key = xor_u
                        new_dp_dict[key] = (new_dp_dict.get(key, 0) + cnt_u * cnt_v) % MOD
                    
                    key = xor_u ^ xor_v
                    new_dp_dict[key] = (new_dp_dict.get(key, 0) + cnt_u * cnt_v) % MOD
            
            dp = list(new_dp_dict.items())
        
        return dp
    
    result_dp = dfs(1, -1)
    
    ans = 0
    for xor_val, cnt in result_dp:
        if xor_val in b_set:
            ans = (ans + cnt) % MOD
    
    print(ans)

def main():
    t = int(input())
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()