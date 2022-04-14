import search
import flask
import threading
import requests
import heapq

allHits = []


@search.app.route('/', methods=['GET'])
def show_GUI():
    """Display / route."""
    query = flask.request.args.get("q")
    weight = flask.request.args.get("w")
    if query and weight:
        # Connect to database
        threads = []
        for url in search.config.SEARCH_INDEX_SEGMENT_API_URLS:
            thread = threading.Thread(
                target=make_query, args=(str(url) + "?q=" + str(query),))
            thread.start()
            threads.append(thread)
        for thread in threads:
            thread.join()
    docList = heapq.merge(*allHits, key=lambda x: x["score"], reverse=True)
    docs = []
    for doc in docList:
        connection = search.model.get_db()
        # Query database
        # find postids of posts posted by logname and users logname is following
        cur = connection.execute(
            "SELECT url, title, summary "
            "WHERE docid = ? ",
            # (doc["docid"])
            (160)
        )
        results = cur.fetchone()
        docs.append(results)
    # Add database info to context
    context = {"docs": docs}
    return flask.render_template("index.html", **context)


def make_query(url):
    print("url = " + url)
    # r = requests.get(url, stream=True)
    # print(r.status_code)
    # print("json = " + str(r.json()))
    # allHits.append(r.json()["hits"])
    # allHits.append({"docid": 5, "score": 5})
    # allHits.append({"docid": 4, "score": 5})
