#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Codeforces Problem E Template
"""

import sys

def input():
    return sys.stdin.readline()

MOD = 998244353
G = 3

def ntt(a, invert):
    n = len(a)
    shift = (n - 1).bit_length()
    
    rev = [0] * n
    for i in range(1, n):
        rev[i] = (rev[i >> 1] >> 1) | ((i & 1) << (shift - 1))
        if i < rev[i]:
            a[i], a[rev[i]] = a[rev[i]], a[i]
    
    length = 2
    while length <= n:
        half = length // 2
        wlen = pow(G, (MOD - 1) // length, MOD)
        if invert:
            wlen = pow(wlen, MOD - 2, MOD)
        
        w = [1] * half
        for i in range(1, half):
            w[i] = (w[i-1] * wlen) % MOD
        
        for i in range(0, n, length):
            for j in range(half):
                u = a[i + j]
                v = (a[i + j + half] * w[j]) % MOD
                a[i + j] = (u + v) % MOD
                a[i + j + half] = (u - v) % MOD
        length <<= 1

    if invert:
        inv_n = pow(n, MOD - 2, MOD)
        for i in range(n):
            a[i] = (a[i] * inv_n) % MOD

def poly_mul(A, B):
    n = len(A)
    m = len(B)
    if n == 0 or m == 0:
        return []
    
    if n * m <= 4000:
        res = [0] * (n + m - 1)
        for i in range(n):
            if A[i] == 0: continue
            for j in range(m):
                res[i+j] = (res[i+j] + A[i] * B[j]) % MOD
        return res
        
    sz = 1
    while sz < n + m - 1:
        sz <<= 1
    a = A + [0] * (sz - n)
    b = B + [0] * (sz - m)
    
    ntt(a, False)
    ntt(b, False)
    for i in range(sz):
        a[i] = (a[i] * b[i]) % MOD
    ntt(a, True)
    
    return a[:n+m-1]

def solve():
    """
    Main solution function for problem E
    """
    n_str = input().strip()
    if not n_str:
        return
    n = int(n_str)
    T = input().strip()
    
    L = n // 2
    T1 = T[:L]
    T2 = T[L:]
    
    divs = []
    for i in range(1, int(L**0.5) + 1):
        if L % i == 0:
            divs.append(i)
            if i * i != L:
                divs.append(L // i)
    divs.sort()
    
    E = {}
    for d in divs:
        A_char = []
        valid = True
        for i in range(d):
            has_a, has_b = False, False
            for j in range(i, L, d):
                if T1[j] == 'a': has_a = True
                elif T1[j] == 'b': has_b = True
            
            if has_a and has_b:
                A_char.append('!')
                valid = False
            elif has_a: A_char.append('a')
            elif has_b: A_char.append('b')
            else: A_char.append('?')
        
        B_char = []
        for i in range(d):
            has_a, has_b = False, False
            for j in range(i, L, d):
                if T2[j] == 'a': has_a = True
                elif T2[j] == 'b': has_b = True
                
            if has_a and has_b:
                B_char.append('!')
                valid = False
            elif has_a: B_char.append('a')
            elif has_b: B_char.append('b')
            else: B_char.append('?')
        
        if not valid:
            E[d] = 0
            continue
        
        A_q = [1 if c == '?' else 0 for c in A_char]
        B_q = [1 if c == '?' else 0 for c in B_char]
        
        A_diff = [1 if c == 'a' else (MOD-1 if c == 'b' else 0) for c in A_char]
        B_diff = [1 if c == 'a' else (MOD-1 if c == 'b' else 0) for c in B_char]
        
        B_q_rev = [B_q[0]] + B_q[d-1:0:-1]
        B_diff_rev = [B_diff[0]] + B_diff[d-1:0:-1]
        
        res_q = poly_mul(A_q, B_q_rev)
        res_diff = poly_mul(A_diff, B_diff_rev)
        
        if len(res_q) < 2 * d - 1:
            res_q += [0] * (2 * d - 1 - len(res_q))
        if len(res_diff) < 2 * d - 1:
            res_diff += [0] * (2 * d - 1 - len(res_diff))
            
        N_Aq, N_Bq = sum(A_q), sum(B_q)
        ans = 0
        
        for k in range(d):
            C_k = (res_q[k] + (res_q[k+d] if k+d < 2*d-1 else 0)) % MOD
            D_k = (res_diff[k] + (res_diff[k+d] if k+d < 2*d-1 else 0)) % MOD
            
            M_k = (d - N_Aq - N_Bq + C_k - D_k) % MOD
            if M_k == 0:
                ans = (ans + pow(2, C_k, MOD)) % MOD
                
        E[d] = ans
        
    H = {d: (E[d] * pow(d, MOD - 2, MOD)) % MOD for d in divs}
    G_over_m = {}
    
    for d in divs:
        val = H[d]
        for x in divs:
            if x < d and d % x == 0:
                val = (val - G_over_m[x]) % MOD
        G_over_m[d] = val
        
    total_S = 0
    for d in divs:
        total_S = (total_S + G_over_m[d] * d) % MOD
        
    print(total_S)

def main():
    """
    Handle multiple test cases if needed
    """
    t_str = input().strip()
    if not t_str:
        return
    t = int(t_str)
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()