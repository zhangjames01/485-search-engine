#!/usr/bin/env python3
"""Word count reducer."""
import sys
import itertools

def reduce_one_group(key, group):
    """Reduce one group."""
    inversedocfreq = group[0].split("\t")[2]
    print(f"{key}\t{inversedocfreq}", end = "\t")
    for line in group:
        word, docId, inversefreq, freq, norm = line.split("\t")
        print(f"{docId}\t{freq}\t{norm}", end="\t")
    print("")

def keyfunc(line):
    """Return the key from a TAB-delimited key-value pair."""
    return line.partition("\t")[0]

def main():
    """Divide sorted lines into groups that share a key."""
    for key, group in itertools.groupby(sys.stdin, keyfunc):
        reduce_one_group(key, group)

if __name__ == "__main__":
    main()