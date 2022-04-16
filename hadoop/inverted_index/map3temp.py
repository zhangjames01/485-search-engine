#!/usr/bin/env python3
"""Map 2."""

import re
import sys

# this will open the file
def main():
    """Map stage."""
    for line in sys.stdin:
        docId, word, inverseFreq, freq, norm = line.strip().split("\t")
        print(f"{word}\t{docId}\t{inverseFreq}\t{freq}\t{norm}")

if __name__ == "__main__":
    main()

