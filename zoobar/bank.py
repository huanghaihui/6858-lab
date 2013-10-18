from zoodb import *
from debug import *

import auth_client
import time

def transfer(sender, recipient, zoobars, token):
    if not auth_client.check_token(sender, token):
        raise AttributeError()

    if zoobars <= 0:
        raise ValueError()

    bankdb = bank_setup()
    senderp = bankdb.query(Bank).get(sender)
    recipientp = bankdb.query(Bank).get(recipient)

    if senderp == recipientp:
        raise AttributeError()

    sender_balance = senderp.zoobars - zoobars
    recipient_balance = recipientp.zoobars + zoobars

    if sender_balance < 0 or recipient_balance < 0:
        raise ValueError()

    senderp.zoobars = sender_balance
    recipientp.zoobars = recipient_balance
    bankdb.commit()

    transfer = Transfer()
    transfer.sender = sender
    transfer.recipient = recipient
    transfer.amount = zoobars
    transfer.time = time.asctime()

    transferdb = transfer_setup()
    transferdb.add(transfer)
    transferdb.commit()

def balance(username):
    db = bank_setup()
    bank = db.query(Bank).get(username)
    return bank.zoobars

def register(username):
    db = bank_setup()
    newbank = Bank()
    newbank.username = username
    db.add(newbank)
    db.commit()

def get_log(username):
    db = transfer_setup()
    return db.query(Transfer).filter(or_(Transfer.sender==username,
                                         Transfer.recipient==username))

