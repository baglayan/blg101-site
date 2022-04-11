import os
from bottle import Bottle, request, run, route

@route('/')
def hello():
    client_ip = request.environ.get('REMOTE_ADDR')
    return ['Your IP is: {}\n'.format(client_ip)]

run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))