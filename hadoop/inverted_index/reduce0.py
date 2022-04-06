"""Reduce 0."""
#!/usr/bin/env python3
"""Word count reducer."""
import sys
import itertools


def reduce_one_group(key, group):
    """Reduce one group."""
    docs = []
    for line in group:
        value = line.partition("\t")[2]
        if value not in docs:
            docs.append(value)
        
    len(docs)


def keyfunc(line):
    """Return the key from a TAB-delimited key-value pair."""
    return line.partition("\t")[0]


def main():
    """Divide sorted lines into groups that share a key."""
    with open()
    for key, group in itertools.groupby(sys.stdin, keyfunc):
        reduce_one_group(key, group)


if __name__ == "__main__":
    main()