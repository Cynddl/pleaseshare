# redefine the settings you want here
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'test.sqlite',           # Or path to database file if using sqlite3. Absolute path needed.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

# Log file, set to '' to disable logging. Absolute path needed
LOG_FILE = '/tmp/example.log'
# Max file size (in MiB)
MAX_SIZE = 10
# Allow compressed archives to be decompressed or not
# (more CPU/RAM usage on upload), used only with OPTION_MULTIFILE
OPTION_DECOMPRESS = True
# Show a link to download the file directly or not
OPTION_DDL = False
# Show the "trackers" field when uploading
OPTION_TRACKERS = True
# Show the "webseeds" field when uploading
OPTION_WEBSEEDS = True
# Show the "Extract" field when uploading
OPTION_MULTIFILE = True
# Allow the creation of private torrents (w/o DHT & PEX)
OPTION_PRIVATE = False
# Default trackers to put in the "trackers" field
#DEFAULT_TRACKERS = []
DEFAULT_TRACKERS = ["udp://tracker.openbittorrent.com:80",
                        "udp://tracker.ccc.de:80"]
# Trackers the torrent will be forced to use (even if OPTION_TRACKERS is False)
MANDATORY_TRACKERS = []
# Directory where all the torrents will get linked to, in order to auto-add them
# in a client (which creates an entry in the DHT, and creates an initial peer)
TORRENT_POOL = '/tmp/pool'
