"""Insta485 REST API."""
import flask
import index
import pathlib
import os
from index.api.main import startup 
from index.api.main import show_hits

"""Insta485 package initializer."""
# app is a single object used by all the code modules in this package



@index.app.route('/api/v1/')
def get_services():
    """Get URL resource URL services."""
    context = {
        "hits": "/api/v1/hits/",
        "url": flask.request.path,
    }
    return flask.jsonify(**context)
