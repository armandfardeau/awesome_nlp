import os
from flask_caching import Cache

config = {
    "DEBUG": os.environ.get("FLASK_DEBUG"),
    "CACHE_TYPE": "FileSystemCache",
    "CACHE_DIR": "/app/tmp/cache",
    "CACHE_THRESHOLD": 10000
}
cache = Cache()
