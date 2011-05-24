from organism.system.controllers import Controller

class HomeController(Controller):
    
    def index(self):
        #return self.redirect("http://google.com")
        
        model          = {}
        model["title"] = "Welcome to uWSGI"
        model["name"]  = "Adam"
        
        self.context.response.cookies.add_cookie("foo", "bar")
        
        return self.view("index.html", model)        