#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Codeforces Problem C Template
"""

import sys

input = sys.stdin.readline

def solve():
    try:
        line1 = input().split()
        if not line1: return
        n = int(line1[0])
        k = int(line1[1])
    except ValueError:
        return

    col_masks = [0] * n
    
    for _ in range(k):
        s = input().strip()
        for i, char in enumerate(s):
            col_masks[i] |= (1 << (ord(char) - 97))

    for d in range(1, n + 1):
        if n % d == 0:
            pattern = []
            possible = True
            
            for i in range(d):
                common_mask = (1 << 26) - 1
                
                current_col = i
                while current_col < n:
                    common_mask &= col_masks[current_col]
                    if common_mask == 0:
                        break
                    current_col += d
                
                if common_mask == 0:
                    possible = False
                    break
                
                chosen_char = ''
                for bit in range(26):
                    if (common_mask >> bit) & 1:
                        chosen_char = chr(bit + 97)
                        break
                pattern.append(chosen_char)

            if possible:
                result = "".join(pattern) * (n // d)
                print(result)
                return

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