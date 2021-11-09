# (c) @AbirHasan2005

import os


class Config(object):
    SESSION_NAME = os.environ.get("SESSION_NAME")
    API_ID = int(os.environ.get("8626831", 8626831))
    API_HASH = os.environ.get("db23330a6edf4a517ee186b35cedec71")
    BOT_TOKEN = os.environ.get("2111558373:AAEJpYwWbrzMXjCvfHdix7m2imhXsywF57Y")
    MAX_INLINE_RESULTS = int(os.environ.get("MAX_INLINE_RESULTS", 50))
