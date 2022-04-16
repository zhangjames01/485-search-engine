#!/usr/bin/env python3
"""Word count reducer."""

import sys
import itertools
import logging


def reduce_one_group(key, group):
    """Reduce one group."""
    sum = 0
    for line in group:
        value = line.split("\t")[1]
        #logging.debug(str(value))
        sum += int(value)
    return sum


def keyfunc(line):
    """Return the key from a TAB-delimited key-value pair."""
    return line.partition("\t")[0]


def main():
    """Divide sorted lines into groups that share a key."""
    count = 0
    for key, group in itertools.groupby(sys.stdin, keyfunc):
        count += reduce_one_group(key, group)
    print(f"{count}")

if __name__ == "__main__":
    main()