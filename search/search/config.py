"""search development configuration."""
import pathlib
# Root of this application, useful if it doesn't occupy an entire domain
APPLICATION_ROOT = '/'
# Secret key for encrypting cookies
# SECRET_KEY = b'r\xa9\xf7\
#     xcd\x94\xcf\xdds\xbd\xa4\x1dc\xd6\xef\x014\xc2P~f\x9f\xd8\x1fN'
# File Upload to var/uploads/
INDEX_ROOT = pathlib.Path(__file__).resolve().parent.parent
MAX_CONTENT_LENGTH = 16 * 1024 * 1024
# Database file is var/search.sqlite3
DATABASE_FILENAME = 'var/index.sqlite3'
SEARCH_INDEX_SEGMENT_API_URLS = [
    #'http://localhost:9000/api/v1/hits/',
    #'http://localhost:9001/api/v1/hits/',
    #'http://localhost:9002/api/v1/hits/',
]
