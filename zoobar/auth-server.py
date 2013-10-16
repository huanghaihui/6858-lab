#!/usr/bin/python

import rpclib
import sys
import auth
from debug import *

class AuthRpcServer(rpclib.RpcServer):
    def rpc_login(self, u, p):
        return auth.login(u, p)

    def rpc_register(self, u, p):
        return auth.register(u, p)

    def rpc_check_token(self, u, t):
        return auth.check_token(u, t)

(_, dummy_zookld_fd, sockpath) = sys.argv

s = AuthRpcServer()
s.run_sockpath_fork(sockpath)
