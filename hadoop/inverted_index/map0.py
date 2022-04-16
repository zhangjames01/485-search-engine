#!/usr/bin/env python3
"""Map 0."""

import re
import sys

# this will open the file
def main():
    """Return the number of documents."""
    dict = {}
    for line in sys.stdin:
        id = line.partition(",")[0]
        dict[id] = 1
    outputDict(dict)
        
def outputDict(dict):
    """Output the dict."""
    for key, value in dict.items():
        print(f"key\t{value}")

if __name__ == "__main__":
    main()

