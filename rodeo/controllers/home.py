from organism.system.controllers import Controller

class HomeController(Controller):
    
    def index(self):
        #return self.redirect("http://google.com")
        
        model          = {}
        model["title"] = "Welcome to uWSGI"
        model["name"]  = "Adam"
        
        #self.context.response.write(self.context.request.cookies["pogo;=Nano=1;"])
        #self.context.response.cookies.add("pogo;=Nano=1;", "dog?;goober;=chunk")
        self.context.response.cookies.add("pogo", "cat", path="/", expires="Sat, 25-May-2013 05:38:18 GMT", httponly=True)
        
        return self.view("index.html", model)        