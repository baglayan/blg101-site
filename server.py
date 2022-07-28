import os
from bottle import Bottle, run, route, error, get, post, request, template, static_file, view
from hashlib import sha256

address_dict = {}
hsh = '848bd78742f569ec15384f796857898594569b5a9edab251033bee5219726e85'


@get('/')
def index():
    client_ip = request.environ.get('HTTP_X_FORWARDED_FOR', '127.0.0.1')
    if client_ip in address_dict:
        address_dict[client_ip] = address_dict.get(client_ip) + 1
    else:
        address_dict[client_ip] = 1
    return template('./site/index.tpl', address_dict = address_dict, current_ip_address = client_ip)

@route('/about')
def about():
    client_ip = request.environ.get('HTTP_X_FORWARDED_FOR', '127.0.0.1')
    return template('./site/about.tpl', current_ip_address = client_ip)

@route('/photos')
def photos():
    client_ip = request.environ.get('HTTP_X_FORWARDED_FOR', '127.0.0.1')
    return template('./site/photos.tpl', current_ip_address = client_ip)

@route('/static/<filename:path>')
def server_static(filename):
    return static_file(filename)

@post('/')
def reset_list():
    entered_password = request.forms.get('password')
    entered_password_hash = sha256(entered_password.encode()).hexdigest()
    if entered_password_hash == hsh:
        global address_dict
        address_dict = {}
        return template('./site/secure.tpl', message="Correct password", information="The list has been reset", current_ip_address = request.environ.get('HTTP_X_FORWARDED_FOR', '127.0.0.1'))
    else:
        return template('./site/secure.tpl', message="Incorrect password", information="The list has not been reset", current_ip_address = request.environ.get('HTTP_X_FORWARDED_FOR', '127.0.0.1'))

@get('/response')
def unreachable():
    return 'Huh.'

@post('/response')
def survey_response():
    rating = request.forms.get('rating')
    if rating == 'positive':
        return template('./site/warning.tpl', message="I'm glad!", information="You can always email me at baglayan19@itu.edu.tr", current_ip_address = request.environ.get('HTTP_X_FORWARDED_FOR', '127.0.0.1'))
    elif rating == 'negative':
        return template('./site/warning.tpl', message="That's saddening!", information="Email me at baglayan19@itu.edu.tr to tell what's wrong", current_ip_address = request.environ.get('HTTP_X_FORWARDED_FOR', '127.0.0.1'))
    elif rating == 'neutral':
        return template('./site/warning.tpl', message="Please spend more time on the site!", information="Email me at baglayan19@itu.edu.tr if you're confused", current_ip_address = request.environ.get('HTTP_X_FORWARDED_FOR', '127.0.0.1'))
    else:
        return template('./site/warning.tpl', message="Is it possible to learn this power?", information="How did you achieve to arrive at this page?", current_ip_address = request.environ.get('HTTP_X_FORWARDED_FOR', '127.0.0.1'))

@error(404)
def error404(error):
    return template('./site/warning.tpl', message="404", information="Not found", current_ip_address = request.environ.get('HTTP_X_FORWARDED_FOR', '127.0.0.1'))

@error(500)
def error500(error):
    return template('./site/warning.tpl', message="500", information="Internal server error", current_ip_address = request.environ.get('HTTP_X_FORWARDED_FOR', '127.0.0.1'))


run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))