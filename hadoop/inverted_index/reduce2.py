#!/usr/bin/env python3
"""Word count reducer."""

import sys
import itertools
import math


def reduce_one_group(key, group):
    """Reduce one group."""
    array = []
    docs = {}
    for line in group:
        array.append(line)
    for line in array:
        modded, docId, word, inversefreq, freq = line.strip().split("\t")
        if not docId in docs:
            docs[docId] = math.pow(float(inversefreq) * float(freq), 2)
        else:
            docs[docId] += math.pow(float(inversefreq) * float(freq), 2)
    # for line in array:
    #     docId, word, inversefreq, freq = line.strip().split("\t")
    #     print(f"{docId}\t{word}\t{inversefreq}\t{freq}\t{sum}")
    count = 0
    finalArray = {}
    for line in array:
        modded, docId, word, inversefreq, freq = line.strip().split("\t")
        if not f"{word} {inversefreq}" in finalArray:
            finalArray[f"{word} {inversefreq}"] = f"{docId} {freq} {docs[docId]}"
        else:
            finalArray[f"{word} {inversefreq}"] += f" {docId} {freq} {docs[docId]}"
    for key in sorted(finalArray):
        print(key + " " + finalArray[key])
# def reduce_one_group(key, group, sum):
#     """Reduce one group."""
#     for line in group:
#         docId, word, inversefreq, freq = line.strip().split("\t")
#         print(f"{docId}\t{word}\t{inversefreq}\t{freq}\t{sum}")


def keyfunc(line):
    """Return the key from a TAB-delimited key-value pair."""
    return line.partition("\t")[0]


def main():
    """Divide sorted lines into groups that share a key."""
    for key, group in itertools.groupby(sys.stdin, keyfunc):
        reduce_one_group(key, group)


if __name__ == "__main__":
    main()
