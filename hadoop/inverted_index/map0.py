import re
import sys

"""Map 0."""
# this will open the file
files = 1
allDocs = []
stopWords = []
allWords = {}
with open("/hadoop/inverted_index/stopwords.txt") as stopWordsFile:
    stopWords = stopWordsFile.readlines()
for line in sys.stdin:
    # get doc id, text, title, and clean up, remove stop words
    id, title, text = line.split(",")
    fullDoc = title + " " + text
    fullDoc = re.sub(r"[^a-zA-Z0-9 ]+", "", fullDoc)
    fullDoc = fullDoc.casefold()
    allDocs.append(fullDoc)
    words = fullDoc.split() 
    for word in words:
        if word not in stopWords:
            allWords[word] = id
# dict = {}
# matrix = []
# docId = 0
#     # for every word, we go through each document,
#     # if the word is in the document, we append docid to dict
# wordId = 0
# for word in allWords:
#     dict[word] = []
#     #matrix[docId] = []
#     for doc in allDocs:
#         docWords = doc.split()
#         if word in docWords:
#             dict[word].append(docId)
#             #matrix[docId].append(1)
#         #else:
#             #matrix[docId].append(0)
#         docId += 1
        
# #print(dict)
sys.stdout(allWords)
        
