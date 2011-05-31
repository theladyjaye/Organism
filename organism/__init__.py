from organism.net.request import Request
from organism.net.response import Response
from organism.net.httpcontext import HttpContext

class Organism(object):
    
    def __init__(self, options):
        self.router         = options["router"]() if "router" in options else None
        self.authorization  = options["authorization"]() if "authorization" in options else None
        self.sessions       = options["sessions"] if "sessions" in options else None
        self.cookies        = options["cookies"] if "cookies" in options else None
        self.request_parser = options["request_parser"] if "request_parser" in options else None
        self.views          = options["views"] if "views" in options else None
        
        
    def __call__(self, environ, start_response):
        handlers = {"environ":environ,
                    "request_parser": self.request_parser,
                    "cookies":self.cookies,
                    "session":self.sessions}
                    
        context             = HttpContext()
        context.request     = Request(**handlers)
        context.response    = Response(start_response, self.cookies)
        context.session     = None if self.sessions is None else  self.sessions(context.request)
        context.view_engine = self.views
        context.environ     = environ
        
        result = None
        route  = self.router.fetch_route(context)
        
        #if route.controller.requires_authorization and self.authorization is not None:
        #    if self.authorization.request_is_authorized(request) is False:
                
        
        if route is not None:
            route.context = context
            result = route()
        else:
            return
        
        return context.response(session=context.session, result=result)
