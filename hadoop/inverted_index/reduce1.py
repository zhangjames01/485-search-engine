#!/usr/bin/env python3
"""Word count reducer."""
import sys
import itertools
import math


def reduce_one_group(key, group, totalDocs):
    """Reduce one group."""
    foundDocs = {}
    for line in group:
        value = line.split("\t")[1]
        if not value in foundDocs:
            foundDocs[value] = 1
        else:
            foundDocs[value] += 1 
    #foundDocs.sort()
    numDocs = len(foundDocs)
    inverseFreq = math.log(numDocs/totalDocs, 10)
    word = str(key)
    for doc in foundDocs:
        docId = doc
        freq = foundDocs[doc]
        print(str(f"{word}\t{inverseFreq}\t{docId}\t{freq}"))
#TODO: pass ^^ to job2, where we will group by docID and then find normalization factor for each doc

def keyfunc(line):
    """Return the key from a TAB-delimited key-value pair."""
    return line.partition("\t")[0]


def main():
    """Divide sorted lines into groups that share a key."""
    totalDocs = 0
    with open("total_document_count.txt") as output:
        totalDocs = int(output.read())
    for key, group in itertools.groupby(sys.stdin, keyfunc):
        reduce_one_group(key, group, totalDocs)


if __name__ == "__main__":
    main()