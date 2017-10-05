def app(environ, start_response):
    data = b"Hello, World!\n"
    start_response("200 OK", [
	("Content-Type", "text/plain"),
        ("Content-Length", str(len(data)))
        ])
    query = environ['QUERY_STRING']
    
    #print(query)
    #query = query.split('&')
    #return iter([''.join(["{}\n".format(hlib) for hlib in query])]) #iter([data])
    print(query.replace('&', '\n'))
    return [query.replace('&','\n')]
