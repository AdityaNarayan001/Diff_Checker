#!/usr/bin/env python3
# diffCheck.py
from blessed import Terminal
import sys

term = Terminal()

def read_file(old_filename, new_filename):
    with open(old_filename, 'r') as o:
        old_lines = o.readlines()

    with open(new_filename, 'r') as n:
        new_lines = n.readlines()

    max_len = max(len(old_lines), len(new_lines))
    old_lines += [''] * (max_len - len(old_lines))
    new_lines += [''] * (max_len - len(new_lines))

    for i in range(max_len):
        old_line = old_lines[i].strip()
        new_line = new_lines[i].strip()

        if old_line != new_line:
            print(term.black_on_red(f"Line {i+1:3}"), term.red2(f"--- {old_line}"))
            print(term.black_on_green(f"Line {i+1:3}"), term.green2(f"+++ {new_line}"))
        else:
            print(term.black_on_yellow(f"Line {i+1:3}"), term.snow(f"    {old_line}"))

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(term.red("Usage: python diff_tool.py <old_file> <new_file>"))
        sys.exit(1)

    old_file = sys.argv[1]
    new_file = sys.argv[2]
    read_file(old_file, new_file)