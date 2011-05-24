from organism.net.response import Response
class Action(object):
    def __call__(self):pass
        

class Redirect(Action):
    def __init__(self, url):
        self.url      = url
        self.response = None
        
    def __call__(self):
        self.response.headers.add_header("location", self.url)
        self.response.status = Response.MOVED_TEMPORARILY
        return None
        
class View(Action):
    
    def __init__(self, view, model=None):
        self.view    = view
        self.model   = model
        self.context = None
    
    def __call__(self):
        if self.context.view_engine is not None:
            engine       = self.context.view_engine(self.context)
            engine.view  = self.view
            engine.model = self.model
            return engine()
        else:
            return None
        
            