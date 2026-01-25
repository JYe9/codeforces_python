#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Codeforces Problem F
"""

import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    iterator = iter(input_data)
    
    def next_int():
        return int(next(iterator))

    try:
        num_test_cases = next_int()
    except StopIteration:
        return

    for _ in range(num_test_cases):
        n = next_int()
        ax = next_int()
        ay = next_int()
        bx = next_int()
        by = next_int()
        
        xs = [next_int() for _ in range(n)]
        ys = [next_int() for _ in range(n)]
        
        points = []
        for i in range(n):
            points.append((xs[i], ys[i]))
        
        points.sort(key=lambda p: p[0])
        
        groups = []
        if n > 0:
            current_x = points[0][0]
            current_min_y = points[0][1]
            current_max_y = points[0][1]
            
            for i in range(1, n):
                px, py = points[i]
                if px == current_x:
                    if py < current_min_y: current_min_y = py
                    if py > current_max_y: current_max_y = py
                else:
                    groups.append((current_min_y, current_max_y))
                    current_x = px
                    current_min_y = py
                    current_max_y = py
            groups.append((current_min_y, current_max_y))
            
        prev_low_y = ay
        prev_high_y = ay
        dp_low = 0
        dp_high = 0
        
        for min_y, max_y in groups:
            dist_span = max_y - min_y
            
            cost_from_low_to_low = dp_low + abs(prev_low_y - max_y) + dist_span
            cost_from_high_to_low = dp_high + abs(prev_high_y - max_y) + dist_span
            
            new_dp_low = min(cost_from_low_to_low, cost_from_high_to_low)
            
            cost_from_low_to_high = dp_low + abs(prev_low_y - min_y) + dist_span
            cost_from_high_to_high = dp_high + abs(prev_high_y - min_y) + dist_span
            
            new_dp_high = min(cost_from_low_to_high, cost_from_high_to_high)
            
            dp_low = new_dp_low
            dp_high = new_dp_high
            prev_low_y = min_y
            prev_high_y = max_y
            
        final_from_low = dp_low + abs(prev_low_y - by)
        final_from_high = dp_high + abs(prev_high_y - by)
        
        min_vertical_moves = min(final_from_low, final_from_high)
        
        total_moves = (bx - ax) + min_vertical_moves
        
        print(total_moves)

if __name__ == "__main__":
    solve()