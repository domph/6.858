from debug import *
from zoodb import *
import rpclib

sys.path.append(os.getcwd())
import readconf

def login(username, password):
    host = readconf.read_conf().lookup_host("auth")
    with rpclib.client_connect(host) as c:
        return c.call("login", username = username, password = password)

def register(username, password):
    host = readconf.read_conf().lookup_host("auth")
    with rpclib.client_connect(host) as c:
        return c.call("register", username = username, password = password)

def check_token(username, token):
    print("[client] check token")
    host = readconf.read_conf().lookup_host("auth")
    with rpclib.client_connect(host) as c:
        return c.call("check_token", username = username, token = token)
