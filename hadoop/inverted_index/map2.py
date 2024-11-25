#!/usr/bin/env python3
"""Map 2."""

import re
import sys

# this will open the file


def main():
    """Map stage."""
    for line in sys.stdin:
        word, inverseFreq, docId, freq = line.strip().split('\t')
        print(f"{(int(docId)%3)}\t{docId}\t{word}\t{inverseFreq}\t{freq}")


if __name__ == "__main__":
    main()
