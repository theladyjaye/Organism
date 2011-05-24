class Route(object):

    def __init__(self, label, controller, action):
        self.label      = label
        self.controller = controller
        self.action     = action
        self.context    = None

    def __call__(self):
        
        # consider action_post action_put, action_head, etc 
        #
        # @post
        # def action(self)
        #
        # or
        #
        # @head
        # def action(self)
        #
        
        if self.action in self.controller.__dict__:
            controller  = self.controller(self.context)
            result      = getattr(controller, self.action)()
            return result