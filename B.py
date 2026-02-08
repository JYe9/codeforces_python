#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Codeforces Problem B Template
"""

import sys

input = sys.stdin.readline

def solve():
    try:
        line1 = input().split()
        if not line1: return
        n = int(line1[0])
        x = int(line1[1])
        y = int(line1[2])
        
        a = list(map(int, input().split()))
    except ValueError:
        return

    contributions = []
    total_contribution_sum = 0
    
    for amount in a:
        val = (amount // x) * y
        contributions.append(val)
        total_contribution_sum += val
        
    max_money = -1
    
    for i in range(n):
        current_money = total_contribution_sum - contributions[i] + a[i]
        
        if current_money > max_money:
            max_money = current_money
            
    print(max_money)

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