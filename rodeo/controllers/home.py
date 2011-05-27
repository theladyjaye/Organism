from organism.system.controllers import Controller
import datetime
class HomeController(Controller):
    
    def index(self):
        #return self.redirect("http://google.com")
        
        model          = {}
        model["title"] = "Welcome to uWSGI"
        model["name"]  = "Adam"
        
        #self.context.response.write(self.context.request.cookies["pogo;=Nano=1;"])
        #self.context.response.cookies.add("pogo;=Nano=1;", "dog?;goober;=chunk")
        x = datetime.datetime.today() + datetime.timedelta(days=1)
        self.context.response.cookies.add("pogo", "cat", path="/", expires=x, httponly=True)
        
        return self.view("index.html", model)        