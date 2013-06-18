import urllib2

class httphelper:
    def __init__(self):
        pass
    
    def get(self,url):
        res=urllib2.urlopen(url)
        return res.read().encode("utf-8")
    
    def post(self,url,body):
        res=urllib2.urlopen(url,body)
        return res.read()
        
if __name__ == '__main__':
    http =httphelper()
    print http.post("","")