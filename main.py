#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Codeforces Test Runner
Quick testing script for your solutions
"""

import sys
import subprocess
from pathlib import Path


def run_solution(problem, input_file="input.txt"):
    """
    Run a solution file with input from input.txt
    
    Args:
        problem: Problem letter (A, B, C, D, E, F)
        input_file: Input file path (default: input.txt)
    """
    solution_file = f"{problem}.py"
    
    if not Path(solution_file).exists():
        print(f"Error: {solution_file} not found!")
        return
    
    if not Path(input_file).exists():
        print(f"Error: {input_file} not found!")
        return
    
    print(f"Running {solution_file} with {input_file}...")
    print("-" * 50)
    
    with open(input_file, 'r') as f:
        result = subprocess.run(
            ['python3', solution_file],
            stdin=f,
            capture_output=True,
            text=True
        )
    
    print("Output:")
    print(result.stdout)
    
    if result.stderr:
        print("Errors:")
        print(result.stderr)
    
    print("-" * 50)


def main():
    """
    Main function to run solutions
    """
    if len(sys.argv) < 2:
        print("Usage: python main.py <problem_letter>")
        print("Example: python main.py A")
        print("Available problems: A, B, C, D, E, F, G, H, I")
        return
    
    problem = sys.argv[1].upper()
    
    if problem not in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']:
        print(f"Invalid problem: {problem}")
        print("Available problems: A, B, C, D, E, F, G, H, I")
        return
    
    input_file = "input.txt"
    if len(sys.argv) > 2:
        input_file = sys.argv[2]
    
    run_solution(problem, input_file)


if __name__ == "__main__":
    main()
