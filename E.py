#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Codeforces Problem E Template
"""

import sys

sys.setrecursionlimit(2000)

def solve():
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    iterator = iter(input_data)
    try:
        num_test_cases = int(next(iterator))
    except StopIteration:
        return
        
    results = []
    INF = float('inf')
    
    for _ in range(num_test_cases):
        n = int(next(iterator))
        m = int(next(iterator))
        
        total_cells = n * m
        grid = [int(next(iterator)) for _ in range(total_cells)]
        
        s = [0] * total_cells
        s[0] = grid[0]

        for j in range(1, m):
            s[j] = s[j-1] + grid[j]
            
        for i in range(1, n):
            s[i * m] = s[(i-1) * m] + grid[i * m]
            
        for i in range(1, n):
            row_curr = i * m
            row_prev = (i - 1) * m
            for j in range(1, m):
                up = s[row_prev + j]
                left = s[row_curr + j - 1]
                best_prev = up if up > left else left
                s[row_curr + j] = best_prev + grid[row_curr + j]

        e = [0] * total_cells
        e[total_cells - 1] = grid[total_cells - 1]
        
        row_last = (n - 1) * m
        for j in range(m - 2, -1, -1):
            e[row_last + j] = e[row_last + j + 1] + grid[row_last + j]
            
        for i in range(n - 2, -1, -1):
            idx = i * m + (m - 1)
            e[idx] = e[idx + m] + grid[idx]
            
        for i in range(n - 2, -1, -1):
            row_curr = i * m
            row_next = (i + 1) * m
            for j in range(m - 2, -1, -1):
                down = e[row_next + j]
                right = e[row_curr + j + 1]
                best_next = down if down > right else right
                e[row_curr + j] = best_next + grid[row_curr + j]

        num_diags = n + m - 1
        best_diag = [-INF] * num_diags
        second_diag = [-INF] * num_diags
        
        for i in range(n):
            row_offset = i * m
            for j in range(m):
                idx = row_offset + j
                k = i + j
                
                val = s[idx] + e[idx] - grid[idx]
                
                if val > best_diag[k]:
                    second_diag[k] = best_diag[k]
                    best_diag[k] = val
                elif val > second_diag[k]:
                    second_diag[k] = val
                    
        min_outcome = INF
        
        for i in range(n):
            row_offset = i * m
            for j in range(m):
                idx = row_offset + j
                k = i + j
                
                current_path_val = s[idx] + e[idx] - grid[idx]
                
                val_if_flipped = current_path_val - 2 * grid[idx]
                
                if current_path_val == best_diag[k]:
                    alternative = second_diag[k]
                else:
                    alternative = best_diag[k]
                
                outcome = val_if_flipped if val_if_flipped > alternative else alternative
                
                if outcome < min_outcome:
                    min_outcome = outcome
                    
        results.append(str(min_outcome))
        
    sys.stdout.write('\n'.join(results) + '\n')

if __name__ == "__main__":
    solve()