#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Codeforces Test Runner
Quick testing script for your solutions with auto-verification
"""

import sys
import subprocess
from pathlib import Path

# ANSI color codes for terminal output
class Colors:
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    CYAN = '\033[96m'
    BOLD = '\033[1m'
    RESET = '\033[0m'

# Symbols for test results
PASS = f"{Colors.GREEN}✓{Colors.RESET}"
FAIL = f"{Colors.RED}✗{Colors.RESET}"
WARN = f"{Colors.YELLOW}?{Colors.RESET}"


def load_expected_output(output_file="output.txt"):
    """
    Load expected output from output.txt
    Returns list of expected output lines (stripped)
    """
    if not Path(output_file).exists():
        return None
    
    with open(output_file, 'r') as f:
        lines = f.read().strip().split('\n')
        # Filter out empty lines and strip whitespace
        return [line.strip() for line in lines if line.strip()]


def compare_outputs(actual_lines, expected_lines):
    """
    Compare actual output with expected output line by line
    Returns: (passed_count, total_count, comparison_results)
    """
    results = []
    passed = 0
    
    max_len = max(len(actual_lines), len(expected_lines))
    
    for i in range(max_len):
        actual = actual_lines[i].strip() if i < len(actual_lines) else None
        expected = expected_lines[i].strip() if i < len(expected_lines) else None
        
        if actual is None:
            results.append(('missing', None, expected))
        elif expected is None:
            results.append(('extra', actual, None))
        elif actual == expected:
            results.append(('pass', actual, expected))
            passed += 1
        else:
            results.append(('fail', actual, expected))
    
    return passed, len(expected_lines), results


def print_comparison(results, actual_lines, expected_lines):
    """
    Print a nicely formatted comparison of actual vs expected output
    """
    passed, total, comparisons = results
    
    print(f"\n{Colors.CYAN}{Colors.BOLD}Verification Results:{Colors.RESET}")
    print("=" * 50)
    
    # Calculate column widths for alignment (based on actual text, not color codes)
    got_width = max(
        max((len(c[1]) if c[1] else 9 for c in comparisons), default=3),  # 9 for "(missing)"
        3  # minimum width for "Got"
    )
    exp_width = max(
        max((len(c[2]) if c[2] else 7 for c in comparisons), default=8),  # 7 for "(extra)"
        8  # minimum width for "Expected"
    )
    
    # Header
    print(f"  #   {'Got':<{got_width}}   Expected")
    print("-" * 50)
    
    for i, (status, actual, expected) in enumerate(comparisons, 1):
        # Determine display values and colors
        if status == 'pass':
            symbol = PASS
            got_text = actual or ""
            exp_text = expected or ""
            got_color = Colors.GREEN
            exp_color = Colors.GREEN
        elif status == 'fail':
            symbol = FAIL
            got_text = actual or ""
            exp_text = expected or ""
            got_color = Colors.RED
            exp_color = Colors.YELLOW
        elif status == 'missing':
            symbol = FAIL
            got_text = "(missing)"
            exp_text = expected or ""
            got_color = Colors.RED
            exp_color = Colors.YELLOW
        else:  # extra
            symbol = WARN
            got_text = actual or ""
            exp_text = "(extra)"
            got_color = Colors.YELLOW
            exp_color = Colors.YELLOW
        
        # Pad BEFORE adding colors to ensure proper alignment
        got_padded = got_text.ljust(got_width)
        
        # Build the line with colors applied after padding
        print(f"  {i}   {symbol} {got_color}{got_padded}{Colors.RESET}   {exp_color}{exp_text}{Colors.RESET}")
    
    print("-" * 50)
    
    # Summary
    if passed == total:
        print(f"{Colors.GREEN}{Colors.BOLD}All Correct! {passed}/{total} passed ✓{Colors.RESET}")
    else:
        print(f"{Colors.RED}{Colors.BOLD}Failed: {passed}/{total} passed{Colors.RESET}")
    
    print("=" * 50)


def run_solution(problem, input_file="input.txt", output_file="output.txt", verify=True):
    """
    Run a solution file with input from input.txt
    Optionally verify against expected output
    
    Args:
        problem: Problem letter (A, B, C, D, E, F)
        input_file: Input file path (default: input.txt)
        output_file: Expected output file path (default: output.txt)
        verify: Whether to verify output (default: True)
    """
    solution_file = f"{problem}.py"
    
    if not Path(solution_file).exists():
        print(f"Error: {solution_file} not found!")
        return
    
    if not Path(input_file).exists():
        print(f"Error: {input_file} not found!")
        return
    
    print(f"{Colors.BOLD}Running {solution_file} with {input_file}...{Colors.RESET}")
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
        print(f"{Colors.RED}Errors:{Colors.RESET}")
        print(result.stderr)
    
    print("-" * 50)
    
    # Verification against expected output
    if verify:
        expected_lines = load_expected_output(output_file)
        
        if expected_lines is None:
            print(f"{WARN} {Colors.YELLOW}No {output_file} found - skipping verification{Colors.RESET}")
        elif not expected_lines:
            print(f"{WARN} {Colors.YELLOW}{output_file} is empty - skipping verification{Colors.RESET}")
        else:
            actual_lines = [line for line in result.stdout.strip().split('\n') if line.strip()]
            comparison = compare_outputs(actual_lines, expected_lines)
            print_comparison(comparison, actual_lines, expected_lines)


def main():
    """
    Main function to run solutions
    
    Usage:
        python main.py A            # Run A.py with verification
        python main.py A --no-verify # Run without verification
        python main.py A custom.txt  # Use custom input file
    """
    if len(sys.argv) < 2:
        print("Usage: python main.py <problem_letter> [input_file] [--no-verify]")
        print("Example: python main.py A")
        print("         python main.py A --no-verify")
        print("         python main.py A custom_input.txt")
        print("Available problems: A, B, C, D, E, F, G, H, I")
        return
    
    problem = sys.argv[1].upper()
    
    if problem not in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']:
        print(f"Invalid problem: {problem}")
        print("Available problems: A, B, C, D, E, F, G, H, I")
        return
    
    input_file = "input.txt"
    verify = True
    
    # Parse additional arguments
    for arg in sys.argv[2:]:
        if arg == '--no-verify':
            verify = False
        elif not arg.startswith('--'):
            input_file = arg
    
    run_solution(problem, input_file, verify=verify)


if __name__ == "__main__":
    main()
