#!/usr/bin/env python3
import re
import sys
import logging

"""Map 2."""
# this will open the file
LOGGER = logging.getLogger(__name__)


def main():
    """Map stage."""
    for line in sys.stdin:
        LOGGER.info(line)
        word, inverseFreq, docId, freq = line.strip().split('\t')
        print(f"{docId}\t{word}\t{inverseFreq}\t{freq}")

if __name__ == "__main__":
    main()

