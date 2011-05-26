class Request(object):
    
    def __init__(self, environ, body=None, cookies=None, session=None):
        
        self.path           = environ["PATH_INFO"]
        self.method         = environ.get("REQUEST_METHOD", "GET")
        self.user_agent     = environ.get("HTTP_USER_AGENT", "Unknown")
        self.accepts        = environ.get("HTTP_ACCEPT", "text/plain")
        self.language       = environ.get("HTTP_ACCEPT_LANGUAGE", "en-US")
        self.charset        = environ.get("HTTP_ACCEPT_CHARSET", "utf-8")
        self.remote_address = environ.get("REMOTE_ADDR", "0.0.0.0")
        
        self.cookies = None if cookies is None else cookies(environ.get("HTTP_COOKIE", None))
        
        try:
            length = int(environ.get("CONTENT_LENGTH", "0"))
            self.body = None if body is None else body(length, environ)
        except ValueError, e:
            self.body = None if body is None else body(-1, environ)
        
        #
        #if self.method.upper() == "POST":
        #    try:
        #    
        #        length = int(environ.get("CONTENT_LENGTH", "0"))
        #    
        #        if length > 0:
        #            post = environ.copy()
        #            post["QUERY_STRING"] = ''
        #    
        #            self.post = cgi.FieldStorage(fp=environ["wsgi.input"], 
        #                                         environ=post, 
        #                                         keep_blank_values=True)
        #    except ValueError, e:
        #        pass
        #        
        #if self.post is not None:
        #    print
            