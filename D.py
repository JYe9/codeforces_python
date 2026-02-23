#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Codeforces Problem D Template
"""

import sys
import heapq

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    iterator = iter(input_data)
    
    try:
        t = int(next(iterator))
    except StopIteration:
        return
        
    out = []
    
    for _ in range(t):
        n = int(next(iterator))
        q = int(next(iterator))
        
        a = [0] * (n + 1)
        for i in range(1, n + 1):
            a[i] = int(next(iterator))
            
        min_heaps = [[] for _ in range(n + 1)]
        max_heaps = [[] for _ in range(n + 1)]
        
        for i in range(1, n + 1):
            v = a[i]
            min_heaps[v].append(i)
            max_heaps[v].append(-i)
            
        for i in range(1, n + 1):
            heapq.heapify(min_heaps[i])
            heapq.heapify(max_heaps[i])
            
        SZ = 1
        while SZ < n + 2:
            SZ *= 2
            
        tree_max = [-1] * (2 * SZ)
        tree_len = [0] * (2 * SZ)
        tree_pref = [0] * (2 * SZ)
        tree_suff = [0] * (2 * SZ)
        tree_ans = [0] * (2 * SZ)
        
        for i in range(SZ, 2 * SZ):
            tree_len[i] = 1
        for i in range(SZ - 1, 0, -1):
            tree_len[i] = tree_len[2 * i] + tree_len[2 * i + 1]
            
        def merge(i):
            l, r = 2 * i, 2 * i + 1
            vL, vR = tree_max[l], tree_max[r]
            
            if vL > vR:
                tree_max[i] = vL
                tree_pref[i] = tree_pref[l]
                tree_suff[i] = 0
                tree_ans[i] = tree_ans[l]
            elif vL < vR:
                tree_max[i] = vR
                tree_pref[i] = 0
                tree_suff[i] = tree_suff[r]
                tree_ans[i] = tree_ans[r]
            else:
                tree_max[i] = vL
                if vL == -1:
                    tree_pref[i] = tree_suff[i] = tree_ans[i] = 0
                else:
                    pL, pR = tree_pref[l], tree_pref[r]
                    sL, sR = tree_suff[l], tree_suff[r]
                    lenL, lenR = tree_len[l], tree_len[r]
                    
                    tree_pref[i] = pL + (pR if pL == lenL else 0)
                    tree_suff[i] = sR + (sL if sR == lenR else 0)
                    
                    mid_len = sL + pR
                    added = mid_len * (mid_len + 1) // 2
                    sub1 = sL * (sL + 1) // 2
                    sub2 = pR * (pR + 1) // 2
                    tree_ans[i] = tree_ans[l] + tree_ans[r] + added - sub1 - sub2

        def update(idx, val):
            p = idx + SZ
            tree_max[p] = val
            if val >= 0:
                tree_pref[p] = tree_suff[p] = tree_ans[p] = 1
            else:
                tree_pref[p] = tree_suff[p] = tree_ans[p] = 0
                
            p //= 2
            while p > 0:
                merge(p)
                p //= 2
                
        def get_first(v):
            h = min_heaps[v]
            while h:
                idx = h[0]
                if a[idx] == v:
                    return idx
                heapq.heappop(h)
            return None

        def get_last(v):
            h = max_heaps[v]
            while h:
                idx = -h[0]
                if a[idx] == v:
                    return idx
                heapq.heappop(h)
            return None

        for v in range(1, n + 1):
            f = get_first(v)
            if f is not None:
                l = get_last(v)
                update(f, l - f)
                
        for _ in range(q):
            idx = int(next(iterator))
            new_val = int(next(iterator))
            old_val = a[idx]
            
            if old_val == new_val:
                ans_max = tree_max[1]
                out.append("0 0" if ans_max <= 0 else f"{ans_max} {tree_ans[1]}")
                continue

            old_F_old = get_first(old_val)
            old_F_new = get_first(new_val)
            
            a[idx] = new_val
            heapq.heappush(min_heaps[new_val], idx)
            heapq.heappush(max_heaps[new_val], -idx)
            
            new_F_old = get_first(old_val)
            new_L_old = get_last(old_val)
            new_F_new = get_first(new_val)
            new_L_new = get_last(new_val)
            
            if old_F_old is not None:
                update(old_F_old, -1)
            if new_F_old is not None:
                update(new_F_old, new_L_old - new_F_old)
                
            if old_F_new is not None:
                update(old_F_new, -1)
            if new_F_new is not None:
                update(new_F_new, new_L_new - new_F_new)
                
            ans_max = tree_max[1]
            if ans_max <= 0:
                out.append("0 0")
            else:
                out.append(f"{ans_max} {tree_ans[1]}")
                
    sys.stdout.write('\n'.join(out) + '\n')

if __name__ == "__main__":
    solve()