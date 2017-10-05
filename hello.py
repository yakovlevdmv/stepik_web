def app(environ, start_response):
        data = b"Hello, World!\n"
        start_response("200 OK", [
            ("Content-Type", "text/plain"),
            ("Content-Length", str(len(data)))
        ])
	query = environ['QUERY_STRING']
	query = query.split('&')
        return ["{}\n".format(hlib) for hlib in query] #iter([data])
