class HttpContext(object):
    
    def __init__(self):
        self.request  = None
        self.response = None
        self.views    = None
        self.environ  = None
