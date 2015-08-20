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

# The number of worker processes for handling
# requests. A positive integer generally  in
# the 2-4 x $(NUM_CORES) range.
workers = multiprocessing.cpu_count() * 2 + 1

# The maximum number of simultaneous clients.
# This setting only affects the Eventlet and
# Gevent worker types.
workers_connections = 1000

# The number of seconds to wait for requests
# on a Keep-Alive connection.
keep_alive = 0