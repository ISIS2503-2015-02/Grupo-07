import multiprocessing

# The number of worker processes for handling
# requests. A positive integer generally in
# the 2-4 x $(NUM_CORES) range.
workers = multiprocessing.cpu_count() * 2 + 1

# The type of workers to use.
# A string referring to one of the following
# bundled classes: sync, eventlet, gevent,
# tornado.
worker_class = "gevent"

# The maximum number of simultaneous clients.
# This setting only affects the Eventlet and
# Gevent worker types.
workers_connections = 80

# The number of seconds to wait for requests
# on a Keep-Alive connection.
keep_alive = 0

# A dictionary containing headers and values
# that the front-end proxy uses to indicate
# HTTPS requests.
# secure_scheme_headers = {
#	'X-FORWARDED-PROTOCOL': 'ssl',
#	'X-FORWARDED-PROTO': 'https',
#	'X-FORWARDED-SSL': 'on'
# }