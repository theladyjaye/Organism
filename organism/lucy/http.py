def parse_http_headers(input):
    headers = input.split("\r\n")
    
    def split(item):
        return item.split(":")
    
    return { k.strip().lower():v.strip() for k,v in map(split, headers) }
    
def parse_mime_multipart(boundary, body):
    prefix     = "--"
    params     = {"files":{},
                  "data":{}}
    
    body = body.lstrip()
    
    f_boundary = "--" + boundary + "\r\n"
    
    if(body.startswith(f_boundary)):
        body = body[len(f_boundary):]
        
    parts = body.split(f_boundary)
    
    for part in parts:
        # check from the left first. 
        # If we check from the right first we could hit an empty
        # value, and that throw things out of wack
        header_end  = part.find("\r\n\r\n") 
        headers     = parse_http_headers(part[:header_end])
        disposition = headers.get("content-disposition", "")
     
        if not disposition: continue # malformed disposition -- no op
            
        first_semi_colon = disposition.find(";")

        if disposition[:first_semi_colon] != "form-data": continue #malformed disposition -- no op
       
        disposition = disposition[(first_semi_colon + 1):].replace('"', '')
        
        def split(item):
            item = item.strip()
            return item.split("=")
            
        meta = { k:v for k,v in map(split, disposition.split(";")) }
        
        if not "name" in meta: continue #malformed disposition -- no op
        
        if "filename" not in meta:
            value = part[header_end + 4:] # 4 = \r\n\r\n
            data  = params["data"]
            if meta["name"] not in data:
                data[meta["name"]] = []
            data[meta["name"]].append(value.strip())
        else:
            pass
        
    
    return params
        
        
        
        
     
    