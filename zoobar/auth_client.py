from debug import *
from zoodb import *
import rpclib

def login(username, password):
    with rpclib.client_connect('/authsvc/sock') as c:
        ret = c.call('login', u=username, p=password)
        return ret

def register(username, password):
    with rpclib.client_connect('/authsvc/sock') as c:
        ret = c.call('register', u=username, p=password)
        return ret

def check_token(username, token):
    with rpclib.client_connect('/authsvc/sock') as c:
        ret = c.call('check_token', u=username, t=token)
        return ret
