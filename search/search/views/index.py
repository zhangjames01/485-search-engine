import search
import flask
import threading
import requests
import heapq

@search.app.route('/', methods=['GET'])
def show_GUI():
    """Display / route."""
    query = flask.request.args.get("q")
    weight = flask.request.args.get("w")
    # Connect to database   
    allHits = []
    for url in search.config.SEARCH_INDEX_SEGMENT_API_URLS:
        thread = threading.Thread(make_query,args=(url, allHits))
        thread.start()
    docList = heapq.merge(*allHits, key = lambda x: x["score"], reverse=True)
    docs = []
    for doc in docList:
        connection = search.model.get_db()
        # Query database
        # find postids of posts posted by logname and users logname is following
        cur = connection.execute(
            "SELECT url, title, summary "
            "WHERE docid = ? "
            (doc["docid"])
        )
        results = cur.fetchone()
        docs.append(results)
    # Add database info to context
    context = {"docs": docs}
    return flask.render_template("index.html", **context)

def make_query(url, allHits):
    r = requests.get(url)
    allHits.append(r.json()["hits"])
