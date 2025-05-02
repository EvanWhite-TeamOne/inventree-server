"""Gunicorn configuration script for InvenTree web server."""

import multiprocessing

bind = '127.0.0.1:8000'

workers = multiprocessing.cpu_count() * 2 + 1

max_requests = 1000
max_requests_jitter = 50

#accesslog = "/var/log/inventree/gunicorn_access.log"
#errorlog = "/var/log/inventree/gunicorn_error.log"
#loglevel = "info"

# preload app so that the ready functions are only executed once
preload_app = True
