from debug import *
from zoodb import *
import rpclib

def transfer(sender, recipient, zoobars, token):
    with rpclib.client_connect('/banksvc/sock') as c:
        ret = c.call('transfer', s=sender, r=recipient, z=zoobars, t=token)
        return ret

def balance(username):
    with rpclib.client_connect('/banksvc/sock') as c:
        ret = c.call('balance', u=username)
        return ret

def register(username):
    with rpclib.client_connect('/banksvc/sock') as c:
        ret = c.call('register', u=username)
        return ret
