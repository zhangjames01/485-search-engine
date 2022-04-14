import index
import flask
import os
import re
import math
import pathlib

index.app.config["INDEX_PATH"] = os.getenv(
    "INDEX_PATH", "inverted_index_1.txt")

stopWords = []
invLines = {}
pageRank = {}


@index.app.before_first_request
def startup():
    """Load inverted index, pagerank, and stopwords into memory."""
    index_dir = pathlib.Path(__file__).parent.parent
    read_stopwords(index_dir)
    read_pagerank(index_dir)
    read_inverted_index(index_dir)


def read_stopwords(index_dir):
    with open(index_dir/"stopwords.txt") as stopWordsFile:
        for line in stopWordsFile:
            stopWords.append(line.strip())


def read_pagerank(index_dir):
    with open(index_dir/"pagerank.out") as rankFile:
        for line in rankFile:
            id, value = line.split(",")
            pageRank[id] = value


def read_inverted_index(index_dir):
    with open(index_dir/"inverted_index"/index.app.config["INDEX_PATH"]) as invIndexFile:
        for line in invIndexFile:
            print("running")
            key = line.partition(" ")[0]
            if not key in invLines:
                invLines[key] = {}
            invLines[key]["idf"] = line.split()[1]
            size = (len(line.split()) - 2)//3
            for i in range(size):
                invLines[key][line.split()[2+(3*i)]] = [line.split()
                                                        [3+(3*i)], line.split()[4+(3*i)]]


@index.app.route('/api/v1/hits/')
def show_hits():
    """Show hits page"""
    query = flask.request.args.get('q', default="", type=str)
    weight = flask.request.args.get('w', default=0.5, type=float)
    queryWords = list(query.split())
    allWords = {}
    for word in queryWords:
        word = word.strip()
        word = re.sub(r"[^a-zA-Z0-9 ]+", "", word)
        word = word.casefold()
        if word not in stopWords:
            if word not in allWords:
                allWords[word] = 1
            else:
                allWords[word] += 1

    docList = []
    for word in allWords:
        if word in invLines:
            keys = list(invLines[word].keys())
            keys.pop(0)
            docList.append(set(keys))
        else:
            context = {"hits": []}
            return flask.jsonify(**context)
    finalDocs = list(docList[0].intersection(*docList))
    hits = []
    # finalDocs.sort()
    for doc in finalDocs:
        q = []
        for word in allWords:
            q.append(float(allWords[word]) * float(invLines[word]["idf"]))
        d = []
        for word in allWords:
            d.append(float(invLines[word][doc][0])
                     * float(invLines[word]["idf"]))
        # dot = q*d
        dot = sum(i[0] * i[1] for i in zip(q, d))
        summy = 0
        for num in q:
            summy += math.pow(num, 2)
        norm_q = math.sqrt(summy)
        norm_d = math.sqrt(float(invLines[word][doc][1]))
        tfidf = dot/(norm_q * norm_d)
        score = (weight * float(pageRank[doc])) + ((1-weight) * tfidf)
        hits.append({"docid": int(doc),
                     "score": score})

    context = {"hits": sorted(hits, key=lambda x: x["score"], reverse=True)}
    return flask.jsonify(**context)
