#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Codeforces Problem D Template
"""

import sys

sys.setrecursionlimit(2000)

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    iterator = iter(input_data)
    try:
        num_test_cases = int(next(iterator))
    except StopIteration:
        return

    INF = 10**18
    
    results = []

    configs = [
        (0, 0, -1, -1), # Case A: p<=x, q<=y
        (1, 1, 1, 1),   # Case B: p>=x, q>=y
        (0, 1, -1, 1),  # Case C: p<=x, q>=y
        (1, 0, 1, -1)   # Case D: p>=x, q<=y
    ]

    for _ in range(num_test_cases):
        x = int(next(iterator))
        y = int(next(iterator))
        
        best_real_cost = INF
        final_p = 0
        final_q = 0
        
        for tp, tq, cp, cq in configs:
            dp_cost = [INF, INF, INF, 0] 
            dp_p = [0, 0, 0, 0]
            dp_q = [0, 0, 0, 0]
            
            for i in range(30, -1, -1):
                xb = (x >> i) & 1
                yb = (y >> i) & 1
                bit_val = 1 << i
                
                new_dp_cost = [INF] * 4
                new_dp_p = [0] * 4
                new_dp_q = [0] * 4
                
                cost_add_k1 = cq * bit_val
                cost_add_k2 = cp * bit_val
                
                for state in range(4):
                    curr_cost = dp_cost[state]
                    if curr_cost == INF:
                        continue
                    
                    tight_p = (state >> 1) & 1
                    tight_q = state & 1
                    
                    curr_p = dp_p[state]
                    curr_q = dp_q[state]
                    
                    for k in range(3):
                        bp = 0
                        bq = 0
                        added = 0
                        
                        if k == 1:
                            bq = 1
                            added = cost_add_k1
                        elif k == 2:
                            bp = 1
                            added = cost_add_k2
                        
                        next_tp = tight_p
                        if tight_p:
                            if tp == 0:
                                if bp > xb: continue
                                if bp < xb: next_tp = 0
                            else:
                                if bp < xb: continue
                                if bp > xb: next_tp = 0
                        
                        next_tq = tight_q
                        if tight_q:
                            if tq == 0:
                                if bq > yb: continue
                                if bq < yb: next_tq = 0
                            else:
                                if bq < yb: continue
                                if bq > yb: next_tq = 0
                        
                        next_state = (next_tp << 1) | next_tq
                        new_total = curr_cost + added
                        
                        if new_total < new_dp_cost[next_state]:
                            new_dp_cost[next_state] = new_total
                            new_dp_p[next_state] = curr_p | (bp << i)
                            new_dp_q[next_state] = curr_q | (bq << i)
                
                dp_cost = new_dp_cost
                dp_p = new_dp_p
                dp_q = new_dp_q

            for state in range(4):
                if dp_cost[state] != INF:
                    p = dp_p[state]
                    q = dp_q[state]
                    real_cost = abs(x - p) + abs(y - q)
                    if real_cost < best_real_cost:
                        best_real_cost = real_cost
                        final_p = p
                        final_q = q

        results.append(f"{final_p} {final_q}")

    sys.stdout.write('\n'.join(results) + '\n')

if __name__ == "__main__":
    main()