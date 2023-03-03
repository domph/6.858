from zoodb import *
from debug import *

import hashlib
import random
import pbkdf2
import os

def newtoken(db, cred):
    hashinput = "%s%.10f" % (cred.password, random.random())
    cred.token = hashlib.md5(hashinput.encode('utf-8')).hexdigest()
    db.commit()
    return cred.token

def login(username, password):
    db = cred_setup()
    cred = db.query(Cred).get(username)
    if not cred:
        return None
    if cred.password == pbkdf2.PBKDF2(password, cred.salt).hexread(32):
        return newtoken(db, cred)
    else:
        return None

def register(username, password):
    # cred setup
    cred_db = cred_setup()
    person = cred_db.query(Cred).get(username)
    if person:
        return None
    
    # create cred
    newcred = Cred()
    newcred.username = username
    newcred.salt = os.urandom(32)
    newcred.password = pbkdf2.PBKDF2(password, newcred.salt).hexread(32)
    cred_db.add(newcred)
    cred_db.commit()
  
    return newtoken(cred_db, newcred)

def check_token(username, token):
    db = cred_setup()
    cred = db.query(Cred).get(username)
    if cred and cred.token == token:
        return True
    else:
        return False

    
