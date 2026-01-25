#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Codeforces Problem A: DBMB and the Array
"""

def solve():
    """
    Main solution function for problem A
    """

    line1 = list(map(int, input().split()))
    n = line1[0]
    s = line1[1]
    x = line1[2]
    
    a = list(map(int, input().split()))
    
    current_sum = sum(a)
    
    if current_sum > s:
        print("NO")
    else:
        diff = s - current_sum
        
        if diff % x == 0:
            print("YES")
        else:
            print("NO")


def main():
    """
    Handle multiple test cases if needed
    """
    input_str = input().strip()
    if not input_str:
        return
    t = int(input_str)
    
    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()