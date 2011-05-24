# http://www.quirksmode.org/js/cookies.html
# http://en.wikipedia.org/wiki/HTTP_cookie
# Cookie: name=value; name2=value2
# environ["HTTP_COOKIE"] = name=value; name2=value2
class CookieHandler(object):
    """
    First the name-value pair ('ppkcookie1=testcookie')
    then a semicolon and a space
    then the expiry date in the correct format ('expires=Thu, 2 Aug 2001 20:47:11 UTC')
    again a semicolon and a space
    then the path (path=/)
    'ppkcookie2=another test; expires=Fri, 3 Aug 2001 20:47:11 UTC; path=/'
    """
    def __init__(self, data=None):
        self.collection = []
        
        if data is not None:
            self.parse_cookies(data)
    
    def add_cookie(self, name, value, path="/", **kwargs):
        self.collection.append({"name":name,
                                "value":value,
                                "path":path,
                                "more":kwargs})
    
    def parse_cookies(self, data):
        pass
        
    def items(self):
        return self.collection
        
    def __len__(self):
        return len(self.collection)