from flask import g, render_template, request, Markup

from login import requirelogin
from zoodb import *
from debug import *
from profile import *
import bank_client

def get_log(username):
    db = transfer_setup()
    return db.query(Transfer).filter(or_(Transfer.sender==username,
                                         Transfer.recipient==username))

@catch_err
@requirelogin
def users():
    args = {}
    args['req_user'] = Markup(request.args.get('user', ''))
    if 'user' in request.values:
        persondb = person_setup()
        user = persondb.query(Person).get(request.values['user'])
        if user:
            transferdb = transfer_setup()
            p = user.profile
            if p.startswith("#!python"):
                p = run_profile(user)

            p_markup = Markup("<b>%s</b>" % p)
            args['profile'] = p_markup

            args['user'] = user
            args['user_zoobars'] = bank_client.balance(user.username)
            args['transfers'] = get_log(user.username)
        else:
            args['warning'] = "Cannot find that user."
    return render_template('users.html', **args)
