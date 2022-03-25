from flask import Flask, Blueprint, jsonify, request, render_template, current_app, g
import requests
import lnurl
from lnurl import Lnurl, LnurlResponse, LnurlWithdrawResponse
from flask_migrate import Migrate
from web_app.models import User, db
from hashids import Hashids


# initialize to blueprint
sats = Blueprint("sats", __name__)

# index home page
# make it super simple
@sats.route("/", methods=['POST', 'GET'])
def index():
    return render_template('index.html')

#add a new user route
@sats.route("/wrapper", methods=["POST"])
def create_user():
    print("CREATING A NEW USER...")
    print("FORM DATA:", dict(request.form))
    # todo: create a new user
    #return jsonify({"message": "CREATED OK (TODO)"})
    if "ln_address" and "link" in request.form:
        ln_address = request.form["ln_address"]
        link = request.form["link"]
        print(ln_address)
        print(link)

        # create uniquie link
        pk = 123 # Your object's id
        domain = 'satsbuster.herokuapp.com' # Your domain

        # use the user name and youtube link to create unique link
        hashids = Hashids(salt=ln_address + link, min_length=6)
        link_id = hashids.encode(pk)
        unique_link = 'https://{domain}/{link_id}'.format(domain=domain, link_id=link_id)

        print(unique_link)

        db.session.add(User(ln_address=ln_address, link=link, unique_link=unique_link))
        db.session.commit()

        message = jsonify({"message": "CREATED OK", "ln_address": ln_address, "embed link": link, "unique link": unique_link})
        error_message = jsonify({"message": "OOPS PLEASE SPECIFY A NAME!"})
        
        print(message)
        print(error_message)

        lastUser = User.query.order_by(-User.id).first()

        return render_template('wrapper.html', lastUser=lastUser)
    else:
        return render_template('error.html')


# testing

@sats.route("/test", methods=['POST', 'GET'])
def test():
    # hack to get the latest user name
    # definitely not ideal but should work for this app
    #ln_user = User.query.order_by( asc(User.id) ).all()
    ##user_text = '<ul>'
    ##for user in ln_user:
    ##    user += ('<li>' + user.ln_address + user.link + '</li>')
    ##    user_text += '</ul>'
    ##embed_link = User.query.order_by( asc(User.) ).all()
    #print(ln_user)
    #print(ln_user[-1])
    #print(link)

    myUser = User.query.all()
    print(myUser)
    oneUser = User.query.filter_by(ln_address="yami").first()
    lastUser = User.query.order_by(-User.id).first()

    return render_template('test.html', myUser=myUser, oneUser=oneUser, lastUser=lastUser)

@sats.route("/test_pay", methods=['POST', 'GET'])
def test_pay():
    return render_template('test_pay.html')

#@sats.route("/test", methods=['POST', 'GET'])
#def test():
#    print("bech32: ", bech32)
#    print("hrp: ", bech32_hrp)
#    print("url: ", url)
#    print("host: ", host)
#    print("base: ", base)
#    print("query: ", query)
#    print("query params: ", query_params)
#    
#    #print("handle: ", handle)
#    print("-- decode --")
#    print("scheme: ", ln_url_d_scheme)
#    print("host: ", ln_url_d_host)
#    print("tld: ", ln_url_d_tld)
#    print("host type: ", ln_url_d_host_type)
#    print("path: ", ln_url_d_path)
#    print("query: ", ln_url_d_query)
#
#    # building our own json responses
#    print("-- building LNURL json response")
#    print("json: ", res_json)
#    print("dict: ", res_dict)
#
#    # parsing (not working)
#    #print("-- parsing res --")
#    #print("r: ", r)
#    #print("res: ", res)
#    #print("res ok: ", res_ok)
#    #print("max send: ", res_max_send)
#    #print("max sats: ", res_max_sats)
#    #print("base: ", res_base)
#    #print("query params: ", res_q_params)
#    #print("metadata: ", res_meta1)
#    #print("metadata2: ", res_meta2)
#    #print("metadata3: ", res_meta3)
#    #print("image: ", res_image)
#
#    return render_template('test.html', ln_url=ln_url)

# examples
#>>> import lnurl
#>>> lnurl.encode('https://service.io/?q=3fc3645b439ce8e7')
#Lnurl('LNURL1DP68GURN8GHJ7UM9WFMXJCM99E5K7TELWY7NXENRXVMRGDTZXSENJCM98PJNWXQ96S9', bech32=Bech32('LNURL1DP68GURN8GHJ7UM9WFMXJCM99E5K7TELWY7NXENRXVMRGDTZXSENJCM98PJNWXQ96S9', hrp='lnurl', data=[13, 1, 26, 7, 8, 28, 3, 19, 7, 8, 23, 18, 30, 28, 27, 5, 14, 9, 27, 6, 18, 24, 27, 5, 5, 25, 20, 22, 30, 11, 25, 31, 14, 4, 30, 19, 6, 25, 19, 3, 6, 12, 27, 3, 8, 13, 11, 2, 6, 16, 25, 19, 18, 24, 27, 5, 7, 1, 18, 19, 14]), url=WebUrl('https://service.io/?q=3fc3645b439ce8e7', scheme='https', host='service.io', tld='io', host_type='domain', path='/', query='q=3fc3645b439ce8e7'))
#>>> lnurl.decode('LNURL1DP68GURN8GHJ7UM9WFMXJCM99E5K7TELWY7NXENRXVMRGDTZXSENJCM98PJNWXQ96S9')
#WebUrl('https://service.io/?q=3fc3645b439ce8e7', scheme='https', host='service.io', tld='io', host_type='domain', path='/', query='q=3fc3645b439ce8e7')