import wsgiref.headers
class Headers(object):
    """
        this class is basically a shell for wsgiref.headers.Headers
        Why? trying to keep the access consistent.
        For example to add a Cookie it's Cookies.add()
        So I wanted Headers.add() as well.  Using wsgiref though
        it would have been Headers.add_header. No bueno for me.
    """
    def __init__(self):
        self._headers = wsgiref.headers.Headers([])
    
    def add(self, name, value, **_params):
        self._headers.add_header(name, value, **_params)
    
    def items(self):
        return self._headers.items()