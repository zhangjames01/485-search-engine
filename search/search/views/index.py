"""Make the index server."""
import search
import flask
import threading
import requests
import heapq
from urllib.parse import urlparse
from urllib.parse import parse_qs

allHits = []


@search.app.route('/', methods=['GET'])
def show_GUI():
    """Display / route."""
    query = ""
    if flask.request.args.get("q"):
        query = flask.request.args.get("q")
    weight = flask.request.args.get("w")
    docList = []
    if query:
        queryList = query.split(" ")
        finalQ = "?q="+str(queryList[0])
        for word in queryList:
            if word != queryList[0]:
                finalQ += "+"+word
        if weight:
            finalQ += "&w=" + str(weight)
        # Connect to database
        threads = []
        for url in search.app.config["SEARCH_INDEX_SEGMENT_API_URLS"]:
            thread = threading.Thread(
                target=make_query, args=(url + finalQ,))
            threads.append(thread)
            thread.start()
        for thread in threads:
            thread.join()
        docList = heapq.merge(*allHits, key=lambda x: x["score"], reverse=True)
        allHits.clear()
        print(docList)
    docs = []
    size = 0
    for doc in docList:
        size += 1
        if size > 10:
            break
        connection = search.model.get_db()
        # Query database
        # find postids of posts posted by logname and users logname is following
        cur = connection.execute(
            "SELECT url, title, summary "
            "FROM Documents "
            "WHERE docid = ? ",
            (doc["docid"],)
            # (160)
        )
        results = cur.fetchone()
        # print(str(results))
        docs.append(results)
       
    # Add database info to context
    context = {"docs": docs, "query": query, "weight": weight}
    return flask.render_template("index.html", **context)


def make_query(url):
    """Make the query."""
    r = requests.get(url)
    allHits.append(r.json()["hits"])
    # allHits.append({"docid": 5, "score": 5})
    # allHits.append({"docid": 4, "score": 5})
