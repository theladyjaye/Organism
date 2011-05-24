from organism import Organism
from organism.defaults.router import Router
from organism.defaults.cookies import CookieHandler
from organism.defaults.sessions import RedisSessions
from organism.defaults.body import UrlEncodedBody
from organism.defaults.views import Jinja2View
from organism.defaults.authorization import AuthorizationHandler


from rodeo.controllers.home import HomeController
from rodeo.controllers.catchall import CatchAllController
from rodeo.views import RodeoViewEngine

critter = {"router":Router,
           "body":UrlEncodedBody,
           "cookies":CookieHandler, 
           "sessions":RedisSessions,
           "autorization":AuthorizationHandler,
           "views":Jinja2View}

organism = Organism(critter)
router   = organism.router

router.map_route(label  = "HomePage",  
                 path   = r"^/$",
                 object = {"controller":HomeController, "action":"index"})
                 
router.map_route(label  = "CatchAll",  
                 path   = r".*",
                 object = {"controller":CatchAllController, "action":"index"})

#router.map_route(name   = "Settings",
#                 method = "GET",  
#                 path   = "/settings",
#                 object = {"controller":SettingsController, "action":"index"})
