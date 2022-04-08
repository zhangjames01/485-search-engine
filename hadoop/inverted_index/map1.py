#!/usr/bin/env python3
import re
import sys

from pyparsing import identchars

"""Map 1."""
# this will open the file


def main():
    """Map stage."""
    allDocs = []
    stopWords = []
    allWords = []
    with open("stopwords.txt") as stopWordsFile:
        for line in stopWordsFile:
            stopWords.append(line.strip())
    for line in sys.stdin:
        # get doc id, text, title, and clean up, remove stop words
        id, comma, fullDoc = line.strip().partition(",")
        id = id.replace('"', '')
        #fullDoc = title + " " + text
        fullDoc = re.sub(r"[^a-zA-Z0-9 ]+", "", fullDoc)
        fullDoc = fullDoc.casefold()
        allDocs.append(fullDoc)
        words = fullDoc.split()
        for word in words:
            word = word.strip()
            if word not in stopWords:
                allWords.append((word, id))

    outputDict(allWords)


def outputDict(dict):
    for item in sorted(dict):
        print(f"{item[0]}\t{item[1]}")


if __name__ == "__main__":
    main()
