# http://www.quirksmode.org/js/cookies.html
# http://en.wikipedia.org/wiki/HTTP_cookie
# Cookie: name=value; name2=value2
# environ["HTTP_COOKIE"] = name=value; name2=value2

import urllib
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
        self.cookies = {}
        
        if data is not None:
            self.parse(data)
    
    
    def add(self, name, value, path="/", expires=None, domain=None, secure=None, httponly=None):
        self.cookies[name] = {"value":urllib.quote_plus(value),
                                "path":path,
                                "expires":expires,
                                "domain":domain,
                                "secure":secure,
                                "httponly":httponly
                                }
    
    def header_items(self):
        # Set-Cookie: name=foo; Domain=.foo.com; Path=/; Expires=Wed, 13-Jan-2021 22:23:01 GMT; HttpOnly
        parts  = []
        
        for key in self.cookies:
            
            parts.append(urllib.quote_plus(key) + "=" + self.cookies[key]["value"])
            parts.append("Path=" + self.cookies[key]["path"])
            
            if self.cookies[key]["expires"] is not None:
                parts.append("Expires=" + self.cookies[key]["expires"])
                
            if self.cookies[key]["domain"] is not None:
                parts.append("Domain=" + self.cookies[key]["domain"])
            
            if self.cookies[key]["secure"] is not None:
                parts.append("Secure")
            
            if self.cookies[key]["httponly"] is not None:
                parts.append("HttpOnly")
    
        yield "; ".join(parts)
        
    def items(self):
        for key in self.cookies:
            yield key, self.cookies[key]
            
    def parse(self, data):
        data = [tuple(item.strip().split("=")) for item in data.split(";")]
        
        for item in data:
            self.cookies[urllib.unquote_plus(item[0])] = { "value":urllib.unquote_plus(item[1]) }
        
    
    def __len__(self):
        return len(self.cookies)
    
    def __getitem__(self, key):
        try:
            return self.cookies[key]["value"]
        except KeyError as e:
            return None