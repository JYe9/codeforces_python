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
        t_str = next(iterator, None)
        if not t_str: return
        t = int(t_str)
    except StopIteration:
        return

    MOD = 998244353
    INV2 = (MOD + 1) // 2
    
    out = []

    for _ in range(t):
        n = int(next(iterator))
        x = int(next(iterator))
        y = int(next(iterator))
        s_str = next(iterator)
        
        Z = n + 5
        
        P = 1 << (1 + Z)
        N = 0
        
        for char in s_str:
            if char == '0':
                P <<= 1
                N >>= 1
                
            elif char == '1':
                new_P = N << 1
                new_N = P >> 1
                P, N = new_P, new_N
                
            else: # '?'
                union_mask = P | N
                P = union_mask << 1
                N = union_mask >> 1
        
        final_mask = P | N
        
        A = x
        B = -(x + y)
        C = (n + 1) * y
        
        total_sum = 0
        
        s_bin = bin(final_mask)[2:]
        len_bin = len(s_bin)
        
        for i, bit in enumerate(s_bin):
            if bit == '1':  
                k = (len_bin - 1 - i) - Z
                
                val = A * k * k + B * k + C
                
                total_sum = (total_sum + (val // 2)) % MOD
                
        out.append(str(total_sum))

    sys.stdout.write('\n'.join(out) + '\n')

if __name__ == "__main__":
    solve()