from organism.system.controllers import Controller
import datetime
class HomeController(Controller):
    
    def index(self):
        #return self.redirect("http://google.com")
        
        model          = {}
        model["title"] = "Welcome to uWSGI"
        model["name"]  = "Adam"
        
        httpcontext = self.context
        
        #httpcontext.response.write(self.context.request.cookies["pogo;=Nano=1;"])
        #httpcontext.response.cookies.add("pogo;=Nano=1;", "dog?;goober;=chunk")
        x = datetime.datetime.today() + datetime.timedelta(days=1)
        self.context.response.cookies.add("pogo", "cat", path="/", expires=x, httponly=True)

        
        httpcontext.response.write("Value of Request Param 'lucy': " + str(httpcontext.request.params["lucy"]))
        
        #httpcontext.request.files["file1"]
        #httpcontext.response.write("Value of Lucy: " + httpcontext.request.post["Lucy"])
        return self.view("index.html", model)        