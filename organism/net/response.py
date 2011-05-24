from wsgiref.headers import Headers
class Response(object):
    OK                = "200 OK"
    MOVED_PERMANENTLY = "301 Moved Permanently"
    MOVED_TEMPORARILY = "302 Moved Temporarily"
    FORBIDDEN         = "403 Forbidden"
    NOT_FOUND         = "404 Not Found"

    def __init__(self, handler, cookies=None):
        self.handler = handler
        self.status  = Response.OK
        self.headers = Headers([("content-type", "text/plain; charset=utf-8")])
        self.cookies = None if cookies is None else cookies()
        
    def __call__(self, result=None):
        value = None
        
        if result is not None:
            value = result()
        
        if self.cookies is not None and len(self.cookies) > 0:
            for cookie in self.cookies.items():
                self.headers.add_header("Set-Cookie", "foo=bar; path=/")
            
        self.handler(self.status, self.headers.items())
        
        if value is not None:
            return [value.encode("utf-8")]
            
