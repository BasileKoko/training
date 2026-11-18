import os

APP_HOST=os.environ.get("HOST", "localhost")
APP_PORT=int(os.environ.get("PORT", "8080"))
LOG_LEVEL=os.environ.get("LOG_LEVEL", "DEBUG")