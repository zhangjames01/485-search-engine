import re
import sys

"""Map 0."""
# this will open the file
def main():
    """Return the number of documents."""
    dict = {}
    for line in sys.stdin:
        id = line.partition(",")[0]
        dict[id] = 1
    outputDict(dict)
        
def outputDict(dict):
    for key, value in dict.items():
        print(key, "\t",value)

if __name__ == "__main__":
    main()

