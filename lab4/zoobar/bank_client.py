from debug import *
from zoodb import *
import rpclib

sys.path.append(os.getcwd())
import readconf

def transfer(sender, recipient, zoobars, token):
    host = readconf.read_conf().lookup_host("bank")
    with rpclib.client_connect(host) as c:
        return c.call("transfer", sender = sender, recipient = recipient,
                      zoobars = zoobars, token = token)

def balance(username):
    host = readconf.read_conf().lookup_host("bank")
    with rpclib.client_connect(host) as c:
        return c.call("balance", username = username)
    
def get_log(username):
    host = readconf.read_conf().lookup_host("bank")
    with rpclib.client_connect(host) as c:
        return c.call("get_log", username = username)
    
def register(username):
    host = readconf.read_conf().lookup_host("bank")
    with rpclib.client_connect(host) as c:
        return c.call("register", username = username)
    