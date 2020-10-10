#import pytest, urllib3
#from flask import url_for
try:  
    from urllib2 import urlopen
except ImportError:  
    from urllib.request import urlopen

def test_checkStatus(client, unitRemote):
    api = "/"
    if unitRemote == None:
        assert client.get(api).status_code == 200
    elif unitRemote != None:
        assert urlopen(unitRemote + api).code == 200        

    api = "/info"
    if unitRemote == None:
        assert client.get(api).status_code == 200
    elif unitRemote != None:
        assert urlopen(unitRemote + api).code == 200        
