#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Codeforces Problem E Template
"""

import sys

# Increase recursion depth
sys.setrecursionlimit(300000)
input = sys.stdin.readline

class SegmentTree:
    def __init__(self, data):
        self.n = len(data)
        self.tree = [0] * (4 * self.n)
        self.lazy = [-1] * (4 * self.n)
        self._build(data, 1, 0, self.n - 1)

    def _build(self, data, node, start, end):
        if start == end:
            self.tree[node] = data[start]
        else:
            mid = (start + end) // 2
            self._build(data, 2 * node, start, mid)
            self._build(data, 2 * node + 1, mid + 1, end)
            self.tree[node] = self.tree[2 * node] + self.tree[2 * node + 1]

    def update_zero(self, l, r):
        self._update(1, 0, self.n - 1, l, r)

    def _update(self, node, start, end, l, r):
        if self.lazy[node] != -1:
            self.tree[node] = 0
            if start != end:
                self.lazy[2 * node] = 0
                self.lazy[2 * node + 1] = 0
            self.lazy[node] = -1

        if start > end or start > r or end < l:
            return

        if self.tree[node] == 0:
            return

        if start >= l and end <= r:
            self.tree[node] = 0
            if start != end:
                self.lazy[2 * node] = 0
                self.lazy[2 * node + 1] = 0
            return

        mid = (start + end) // 2
        self._update(2 * node, start, mid, l, r)
        self._update(2 * node + 1, mid + 1, end, l, r)
        self.tree[node] = self.tree[2 * node] + self.tree[2 * node + 1]

    def query_total(self):
        if self.lazy[1] != -1:
            return 0
        return self.tree[1]

def solve():
    try:
        line1 = input().split()
        if not line1: return
        n = int(line1[0])
        a = list(map(int, input().split()))
        c = list(map(int, input().split()))
        p = list(map(int, input().split()))
    except ValueError:
        return

    # 1. Build Cartesian Tree
    left_child = [-1] * n
    right_child = [-1] * n
    parent = [-1] * n  # We need parent pointers to find group roots
    stack = []
    
    for i in range(n):
        last_popped = -1
        # Tie-breaking: stack top is popped if it's smaller OR equal value but more expensive
        while stack and (a[stack[-1]] < a[i] or (a[stack[-1]] == a[i] and c[stack[-1]] > c[i])):
            last_popped = stack.pop()
        
        if last_popped != -1:
            left_child[i] = last_popped
            parent[last_popped] = i
        
        if stack:
            right_child[stack[-1]] = i
            parent[i] = stack[-1]
            
        stack.append(i)
        
    root = stack[0] if stack else 0

    # 2. Precompute Group Roots
    group_root = list(range(n))
    
    grp_stack = [root]
    while grp_stack:
        u = grp_stack.pop()
        p_node = parent[u]
        
        # If parent exists and values are equal, my group root is my parent's group root
        if p_node != -1 and a[p_node] == a[u]:
            group_root[u] = group_root[p_node]
        else:
            # Otherwise, I am the root of my group
            group_root[u] = u
            
        if right_child[u] != -1:
            grp_stack.append(right_child[u])
        if left_child[u] != -1:
            grp_stack.append(left_child[u])

    # 3. DFS for initial costs and Segment Tree mapping
    node_to_pos = [-1] * n
    subtree_exit = [-1] * n
    m_values = []
    
    timer = 0
    dfs_stack = [[root, c[root], 0]] # u, path_min, state
    
    while dfs_stack:
        curr = dfs_stack[-1]
        u = curr[0]
        path_min = curr[1]
        state = curr[2]
        
        if state == 0:
            node_to_pos[u] = timer
            timer += 1
            
            if u == root:
                cost = 0
                next_path_min = c[u]
            else:
                cost = min(c[u], path_min)
                next_path_min = cost
            
            m_values.append(cost)
            
            dfs_stack[-1][2] = 1
            if left_child[u] != -1:
                dfs_stack.append([left_child[u], next_path_min, 0])
                
        elif state == 1:
            dfs_stack[-1][2] = 2
            
            if u == root:
                next_path_min = c[u]
            else:
                next_path_min = min(c[u], path_min)
                
            if right_child[u] != -1:
                dfs_stack.append([right_child[u], next_path_min, 0])
                
        else:
            subtree_exit[u] = timer - 1
            dfs_stack.pop()
            
    # 4. Segment Tree and Updates
    st = SegmentTree(m_values)
    results = []
    results.append(st.query_total())
    
    for idx in p:
        original_target = idx - 1
        target = group_root[original_target]
        
        l, r = node_to_pos[target], subtree_exit[target]
        st.update_zero(l, r)
        
        results.append(st.query_total())
        
    print(*(results))

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