#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Codeforces Problem C Template
"""

import sys

input = sys.stdin.readline

def solve():
    try:
        line1 = input().strip()
        if not line1: return
        n = int(line1)
        
        line2 = input().strip()
        a = list(map(int, line2.split()))
    except ValueError:
        return

    odds = []
    evens = []
    for x in a:
        if x % 2 == 1:
            odds.append(x)
        else:
            evens.append(x)
            
    odds.sort(reverse=True)
    evens.sort(reverse=True)
    
    len_odds = len(odds)
    len_evens = len(evens)
    
    prefix_evens = [0] * (len_evens + 1)
    for i in range(len_evens):
        prefix_evens[i+1] = prefix_evens[i] + evens[i]
        
    results = []
    
    for k in range(1, n + 1):
        if len_odds == 0:
            results.append(0)
            continue
            
        min_odds_needed = k - len_evens
        
        current_i = max(1, min_odds_needed)
        
        if current_i % 2 == 0:
            current_i += 1
            
        if current_i <= len_odds and current_i <= k:
            evens_count = k - current_i
            score = odds[0] + prefix_evens[evens_count]
            results.append(score)
        else:
            results.append(0)
            
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