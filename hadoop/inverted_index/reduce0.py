"""Reduce 0."""
#!/usr/bin/env python3
"""Word count reducer."""
import sys
import itertools


def reduce_one_group(key, group):
    """Reduce one group."""
    count = 0
    for line in group:
        value = line.partition("\t")[2]
        count += value
    


def keyfunc(line):
    """Return the key from a TAB-delimited key-value pair."""
    return line.partition("\t")[0]


def main():
    """Divide sorted lines into groups that share a key."""
    count = 0
    for key, group in itertools.groupby(sys.stdin, keyfunc):
        reduce_one_group(key, group)
        count += 1
    print(count)

if __name__ == "__main__":
    main()