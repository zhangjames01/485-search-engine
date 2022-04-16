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
    if query and weight:
        queryList = query.split(" ")
        print("query = " + str(query))
        # Connect to database
        threads = []
        for url in search.config.SEARCH_INDEX_SEGMENT_API_URLS:
            if len(queryList) == 1:
                thread = threading.Thread(
                    # use request library to get url + query
                    # target=make_query, args=requests.get(url, params={"q": query, "w": weight}))
                    target=make_query, args=(str(url) + "?q=" + str(query) + "&w=" + str(weight),))
                thread.start()
                threads.append(thread)
            else:
                thread = threading.Thread(
                    # use request library to get url + query
                    # target=make_query, args=requests.get(url, params={"q": query, "w": weight}))
                    target=make_query, args=(str(url) + "?q=" + str(queryList[0]) + "+" + str(queryList[1]) + "&w=" + str(weight),))
                thread.start()
                threads.append(thread)
        for thread in threads:
            thread.join()
        docList = heapq.merge(*allHits, key=lambda x: x["score"], reverse=True)
        print(docList)
    docs = []
    for doc in docList:
        connection = search.model.get_db()
        # Query database
        # find postids of posts posted by logname and users logname is following
        cur = connection.execute(
            "SELECT url, title, summary "
            "FROM Documents "
            "WHERE docid = ? ",
            ([doc["docid"]])
            # (160)
        )
        results = cur.fetchone()
        #print(str(results))
        docs.append(results)
    # Add database info to context
    context = {"docs": docs, "query": query}
    return flask.render_template("index.html", **context)


def make_query(url):
    r = requests.get(url)
    print("url = " + str(url))
    print(r.status_code)
    print("json = " + str(r.json()))
    allHits.append(r.json()["hits"])
    # allHits.append({"docid": 5, "score": 5})
    # allHits.append({"docid": 4, "score": 5})
