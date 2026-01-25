#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Codeforces Problem G
"""

import sys

sys.setrecursionlimit(300000)

def get_response():
    while True:
        line = sys.stdin.readline()
        if not line: 
            sys.exit(0)
        line = line.strip()
        if line:
            val = int(line)
            if val == -1:
                sys.exit(0)
            return val

def solve():
    while True:
        line = sys.stdin.readline()
        if not line: return
        line = line.strip()
        if line:
            n = int(line)
            break
            
    adj = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        while True:
            edge_line = sys.stdin.readline()
            if edge_line.strip():
                u, v = map(int, edge_line.split())
                adj[u].append(v)
                adj[v].append(u)
                break

    dfs_order = []
    visited = [False] * (n + 1)
    
    stack = [1]
    visited[1] = True
    
    while stack:
        u = stack.pop()
        dfs_order.append(u)
        
        for v in adj[u]:
            if not visited[v]:
                visited[v] = True
                stack.append(v)
    
    for i in range(0, n - 1, 2):
        u = dfs_order[i]
        v = dfs_order[i+1]
        
        print(f"? {u} {v}")
        sys.stdout.flush()
        
        res = get_response()
        
        if res == 1:
            print(f"? {u} {u}")
            sys.stdout.flush()
            
            res2 = get_response()
            
            if res2 == 1:
                print(f"! {u}")
            else:
                print(f"! {v}")
            sys.stdout.flush()
            return
            
    print(f"! {dfs_order[-1]}")
    sys.stdout.flush()

def main():
    line = sys.stdin.readline()
    if not line: return
    try:
        t = int(line)
    except ValueError: return
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()