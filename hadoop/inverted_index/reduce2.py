#!/usr/bin/env python3
"""Word count reducer."""
import sys
import itertools
import math

def reduce_one_group(key, group):
    """Reduce one group."""
    sum = 0
    for line in group:
        
        sum += math.pow(line.split("\t")[2] * line.split("\t")[3], 2)
    for line in group:
        docId, word, inversefreq, freq = line.split("\t")
        print(f"{docId}\t{word}\t{inversefreq}\t{freq}\t{sum}")

def keyfunc(line):
    """Return the key from a TAB-delimited key-value pair."""
    return line.partition("\t")[0]

def main():
    """Divide sorted lines into groups that share a key."""
    for key, group in itertools.groupby(sys.stdin, keyfunc):
        reduce_one_group(key, group)

if __name__ == "__main__":
    main()