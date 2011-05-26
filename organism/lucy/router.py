import re
from organism.system.routes import Route
class Router(object):
    
    def __init__(self):
        self.routes = {}
    
    def fetch_route(self, context):
        collection = None
        route      = None
        request    = context.request
        # if specified, look though the method collection first
        if request.method in self.routes:
            collection = self.routes[request.method]
            route      = self.find_route_in_collection(collection, request.path)
            
        if route is not None : return route
            
        # still got nothing? Look trough the global collection
        collection = self.routes["*"]
        route      = self.find_route_in_collection(collection, request.path)
        
        if route is not None : return route
        
        return None
        
    def find_route_in_collection(self, collection, path):
        
        for candidate in collection:
            if candidate["path"].match(path):
                
                args = {"label":candidate["label"], 
                        "controller":candidate["object"]["controller"], 
                        "action":candidate["object"]["action"]}
                
                return Route(**args)
        
        return None
                
    def map_route(self, label, path, object, method="*"):
        method = method.upper()
        if method not in self.routes:
            self.routes[method] = []
            
        self.routes[method].append({"path":re.compile(path), "label": label, "object":object})
