from organism.system.actions import View
from organism.system.actions import Redirect

class Controller(object):
    
    def __init__(self, context):
        self.context = context
    
    def redirect(self, url):
        redirect          = Redirect(url)
        redirect.response = self.context.response
        return redirect
        
    def view(self, view_path, model):
        view         = View(view_path, model)
        view.context = self.context
        return view