#!/usr/bin/python

import rpclib
import sys
import bank
from debug import *

class BankRpcServer(rpclib.RpcServer):
    def rpc_transfer(self, s, r, z):
        return bank.transfer(s, r, z)

    def rpc_balance(self, u):
        return bank.balance(u)

    def rpc_register(self, u):
        return bank.register(u)

(_, dummy_zookld_fd, sockpath) = sys.argv

s = BankRpcServer()
s.run_sockpath_fork(sockpath)
