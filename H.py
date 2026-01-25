#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Codeforces Problem H
"""

import sys
import heapq

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

    for _ in range(num_test_cases):
        try:
            n = int(next(iterator))
        except StopIteration:
            break
            
        a = [0] + [int(next(iterator)) for _ in range(n)]
        
        adj = [[] for _ in range(n + 1)]
        for _ in range(n - 1):
            u = int(next(iterator))
            v = int(next(iterator))
            adj[u].append(v)
            adj[v].append(u)
            
        dp = [[False] * 2 for _ in range(n + 1)]
        
        def dfs_dp(u, p):
            for v in adj[u]:
                if v == p:
                    continue
                dfs_dp(v, u)
            
            for p_dir in range(2):
                parent_val = 0
                if p_dir == 1 and p != 0:
                    parent_val = a[p]
                
                target_parity = (a[u] + 1 - parent_val) % 2
                
                current_sum = 0
                flexible_odd_exists = False
                possible = True
                
                for v in adj[u]:
                    if v == p:
                        continue
                    
                    can_u_to_v = dp[v][0]
                    
                    can_v_to_u = dp[v][1]
                    
                    if not can_u_to_v and not can_v_to_u:
                        possible = False
                        break
                    
                    if can_u_to_v and not can_v_to_u:
                        current_sum += a[v]
                    elif not can_u_to_v and can_v_to_u:
                        current_sum += 0
                    else:
                        if a[v] % 2 != 0:
                            flexible_odd_exists = True
                
                if possible:
                    needed = (target_parity - current_sum) % 2
                    if needed == 0:
                        dp[u][p_dir] = True
                    elif needed == 1 and flexible_odd_exists:
                        dp[u][p_dir] = True
                    else:
                        dp[u][p_dir] = False
                else:
                    dp[u][p_dir] = False

        dfs_dp(1, 0)
        
        if not dp[1][0]:
            print("NO")
        else:
            print("YES")
            
            queue = [(1, 0, 0)]
            directed_edges = []
            
            while queue:
                u, p, p_dir = queue.pop()
                
                if p != 0:
                    if p_dir == 1: # u -> p
                        directed_edges.append((u, p))
                    else:          # p -> u
                        directed_edges.append((p, u))
                
                parent_val = 0
                if p_dir == 1 and p != 0:
                    parent_val = a[p]
                
                target_parity = (a[u] + 1 - parent_val) % 2
                current_sum = 0
                flexible_nodes = []
                child_decisions = {} 
                
                for v in adj[u]:
                    if v == p: continue
                    
                    can_u_to_v = dp[v][0]
                    can_v_to_u = dp[v][1]
                    
                    if can_u_to_v and not can_v_to_u:
                        child_decisions[v] = 1
                        current_sum += a[v]
                    elif not can_u_to_v and can_v_to_u:
                        child_decisions[v] = 0
                    else:
                        flexible_nodes.append(v)
                
                needed = (target_parity - current_sum) % 2
                
                flipped = False
                for v in flexible_nodes:
                    if needed == 1 and not flipped and a[v] % 2 != 0:
                        child_decisions[v] = 1
                        flipped = True
                    else:
                        child_decisions[v] = 0
                        
                for v in adj[u]:
                    if v == p: continue
                    decision = child_decisions[v]
                    next_p_dir = 0 if decision == 1 else 1
                    queue.append((v, u, next_p_dir))
            
            in_degree = [0] * (n + 1)
            graph = [[] for _ in range(n + 1)]
            
            for u, v in directed_edges:
                graph[u].append(v)
                in_degree[v] += 1
            
            topo_queue = [i for i in range(1, n + 1) if in_degree[i] == 0]
            heapq.heapify(topo_queue)
            
            result = []
            
            while topo_queue:
                curr = heapq.heappop(topo_queue)
                result.append(curr)
                
                for neighbor in graph[curr]:
                    in_degree[neighbor] -= 1
                    if in_degree[neighbor] == 0:
                        heapq.heappush(topo_queue, neighbor)
            
            print(*(result))

if __name__ == "__main__":
    solve()