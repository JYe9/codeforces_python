#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Codeforces Problem E Template
"""

import sys
sys.setrecursionlimit(300000)

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    iterator = iter(input_data)
    
    try:
        num_test_cases = int(next(iterator))
    except StopIteration:
        return

    output = []

    for _ in range(num_test_cases):
        n = int(next(iterator))
        m = int(next(iterator))

        parent = [i + 1 for i in range(n + 1)]
        for _ in range(m):
            u = int(next(iterator))
            v = int(next(iterator))
            if v > parent[u]:
                parent[u] = v
        
        adj = [[] for _ in range(n + 1)]
        for i in range(1, n):
            adj[parent[i]].append(i)

        depth = [0] * (n + 1)
        sz = [0] * (n + 1)
        heavy = [0] * (n + 1)
        
        def dfs_init(u, d):
            depth[u] = d
            s = 1
            max_s = -1
            h = 0
            for v in adj[u]:
                dfs_init(v, d + 1)
                s += sz[v]
                if sz[v] > max_s:
                    max_s = sz[v]
                    h = v
            sz[u] = s
            heavy[u] = h

        dfs_init(n, 0)

        total_depth_cnt = [0] * (n + 1)
        for i in range(1, n + 1):
            total_depth_cnt[depth[i]] += 1
            
        suffix_cnt = [0] * (n + 2)
        for d in range(n, -1, -1):
            suffix_cnt[d] = total_depth_cnt[d] + suffix_cnt[d+1]

        term1 = 0
        for i in range(1, n + 1):
            d = depth[i]
            count_valid_jerry = suffix_cnt[d] - 1
            term1 += d * count_valid_jerry

        term2 = 0
        
        cnt = [0] * (n + 1)
        current_sq_sum = 0

        def add(u, root_adj):
            nonlocal current_sq_sum
            d = depth[u]
            
            current_sq_sum += 2 * cnt[d] + 1
            cnt[d] += 1
            
            for v in root_adj[u]:
                add(v, root_adj)

        def remove(u, root_adj):
            nonlocal current_sq_sum
            d = depth[u]
            
            current_sq_sum -= 2 * cnt[d] - 1
            cnt[d] -= 1
            
            for v in root_adj[u]:
                remove(v, root_adj)

        def dsu(u, keep):
            nonlocal term2, current_sq_sum
            
            for v in adj[u]:
                if v != heavy[u]:
                    dsu(v, False)
            
            if heavy[u]:
                dsu(heavy[u], True)
            
            d = depth[u]
            
            current_sq_sum += 2 * cnt[d] + 1
            cnt[d] += 1
            
            for v in adj[u]:
                if v != heavy[u]:
                    add(v, adj)
            
            if u != n:
                s = sz[u]
                val = (s * s + current_sq_sum) // 2 - s
                term2 += val
    
            if not keep:
                remove(u, adj)

        dsu(n, False)

        result = term1 - term2
        output.append(str(result))

    sys.stdout.write('\n'.join(output) + '\n')

if __name__ == "__main__":
    solve()