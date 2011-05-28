import urlparse
class Posts(object):
    
    def __init__(self, content_type, length, data):
        
        self._data = None
        
        if length > 0:
            
            if content_type.startswith("application/x-www-form-urlencoded"):
                self._parse_urlencoded(length, data)
            
            elif content_type.startswith("multipart/form-data"):
                self._parse_multipart(length, data)
    
    def _parse_urlencoded(self, length, data):
        input = data.read(length)
        self._data = urlparse.parse_qs(input)

    def _parse_multipart(self, length, data):pass
    
    def __getitem__(self, key):
        try:
            target = self._data[key]
            return target[0] if len(target) is 1 else target
        except KeyError as e:
            return None