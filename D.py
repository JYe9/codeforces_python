#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Codeforces Problem D Template
"""

import sys

input = sys.stdin.readline

def solve():
    try:
        line1 = input().split()
        if not line1: return
        n = int(line1[0])
        m = int(line1[1])
        
        grid = []
        total_ones = 0
        for _ in range(n):
            row = list(map(int, input().split()))
            total_ones += sum(row)
            grid.append(row)
            
    except ValueError:
        return

    target = total_ones // 2
    
    print(target * (total_ones - target))
    
    heights = [n] * m
    current_ones = total_ones
    
    for col in range(m):
        while heights[col] > 0 and current_ones > target:
            row_to_remove = heights[col] - 1
            val = grid[row_to_remove][col]
            
            if val == 1:
                current_ones -= 1
            
            heights[col] -= 1
            
            if current_ones == target:
                break
        
        if current_ones == target:
            break
            
    path = []
    current_row = 0
    
    for col in range(m):
        target_row = heights[col]
        
        while current_row < target_row:
            path.append('D')
            current_row += 1
            
        path.append('R')
        
    while current_row < n:
        path.append('D')
        current_row += 1
        
    print("".join(path))

def main():
    try:
        t_str = input().strip()
        if not t_str: return
        t = int(t_str)
        for _ in range(t):
            solve()
    except ValueError:
        pass

if __name__ == "__main__":
    main()