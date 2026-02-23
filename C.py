#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Codeforces Problem C Template
"""

import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    t = int(input_data[0])
    out = []
    idx = 1
    
    MOD = 998244353
    
    MAXN = 300005
    pow2 = [1] * MAXN
    for i in range(1, MAXN):
        pow2[i] = (pow2[i-1] * 2) % MOD

    for _ in range(t):
        n = int(input_data[idx])
        S = input_data[idx+1]
        idx += 2
        
        P = [0] * (n + 1)
        for i in range(n):
            P[i+1] = P[i] + (1 if S[i] == '(' else -1)
            
        next_bad = [0] * (n + 2)
        last_bad = n + 1 
        for i in range(n, 0, -1):
            if P[i] <= 1:
                last_bad = i
            next_bad[i] = last_bad
            
        sum_W_close = 0
        active_W_open = 0
        expire = [0] * (n + 2)
        ans = 0
        
        for i in range(1, n + 1):
            W_i = (1 + sum_W_close + active_W_open) % MOD
            
            if S[i-1] == '(':
                ans = (ans + pow2[i-1]) % MOD
                
                N_i = next_bad[i]
                if N_i >= i:
                    active_W_open = (active_W_open + W_i) % MOD
                    if N_i <= n:
                        expire[N_i] = (expire[N_i] + W_i) % MOD
            else:
                ans = (ans + W_i) % MOD
                sum_W_close = (sum_W_close + W_i) % MOD
                
            active_W_open = (active_W_open - expire[i]) % MOD
            
        out.append(str(ans))
        
    print('\n'.join(out))

if __name__ == '__main__':
    solve()