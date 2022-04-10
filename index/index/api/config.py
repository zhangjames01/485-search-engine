"""Insta485 development configuration."""
import pathlib
# Root of this application, useful if it doesn't occupy an entire domain
APPLICATION_ROOT = '/'
# Secret key for encrypting cookies
SECRET_KEY = b'r\xa9\xf7\
    xcd\x94\xcf\xdds\xbd\xa4\x1dc\xd6\xef\x014\xc2P~f\x9f\xd8\x1fN'
SESSION_COOKIE_NAME = 'login'
# File Upload to var/uploads/
INDEX_ROOT = pathlib.Path(__file__).resolve().parent.parent
UPLOAD_FOLDER = INDEX_ROOT/'var'/'uploads'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
MAX_CONTENT_LENGTH = 16 * 1024 * 1024
# Database file is var/insta485.sqlite3
DATABASE_FILENAME = INDEX_ROOT/'var'/'index.sqlite3'
