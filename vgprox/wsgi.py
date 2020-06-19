def app(environ, start_response):
    '''po zaprosu http://127.0.0.1:8000/?a=1&a=3&b=0
    app vozvrashaet v stolbik znacheniya'''
    qs = environ['QUERY_STRING']
    s = qs.replace('&','<br>')
    data = s.encode()
    print(data)
    start_response('200 OK', [('Content-type', 'text/plain')])
    return [data]