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

#ceate a unique link route, adds new creator(user) to the database
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
        # domain = satsbuster.herokuapp.com
        domain = 'www.boltbooster.com' # Your domain

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

@sats.route("/boosting", methods=["POST", "GET"])
def user_page():
    lastUser = User.query.order_by(-User.id).first()
    return render_template('wrapper_user.html',  lastUser=lastUser)


# testing

@sats.route("/test_html", methods=['POST', 'GET'])
def test_aww():
    return render_template('test_aww.html')

@sats.route("/test", methods=['POST', 'GET'])
def test():
    # get latest user
    
    myUser = User.query.all()
    print(myUser)
    oneUser = User.query.filter_by(ln_address="yami").first()
    lastUser = User.query.order_by(-User.id).first()

    return render_template('test.html', myUser=myUser, oneUser=oneUser, lastUser=lastUser)

#@sats.route("/test_pay", methods=['POST', 'GET'])
#def test_pay():
#    return render_template('test_pay.html')

@sats.route("/test_pay", methods=['POST', 'GET'])
def test_pay():
    return render_template('test_send.html')

# examples
#>>> import lnurl
#>>> lnurl.encode('https://service.io/?q=3fc3645b439ce8e7')
#Lnurl('LNURL1DP68GURN8GHJ7UM9WFMXJCM99E5K7TELWY7NXENRXVMRGDTZXSENJCM98PJNWXQ96S9', bech32=Bech32('LNURL1DP68GURN8GHJ7UM9WFMXJCM99E5K7TELWY7NXENRXVMRGDTZXSENJCM98PJNWXQ96S9', hrp='lnurl', data=[13, 1, 26, 7, 8, 28, 3, 19, 7, 8, 23, 18, 30, 28, 27, 5, 14, 9, 27, 6, 18, 24, 27, 5, 5, 25, 20, 22, 30, 11, 25, 31, 14, 4, 30, 19, 6, 25, 19, 3, 6, 12, 27, 3, 8, 13, 11, 2, 6, 16, 25, 19, 18, 24, 27, 5, 7, 1, 18, 19, 14]), url=WebUrl('https://service.io/?q=3fc3645b439ce8e7', scheme='https', host='service.io', tld='io', host_type='domain', path='/', query='q=3fc3645b439ce8e7'))
#>>> lnurl.decode('LNURL1DP68GURN8GHJ7UM9WFMXJCM99E5K7TELWY7NXENRXVMRGDTZXSENJCM98PJNWXQ96S9')
#WebUrl('https://service.io/?q=3fc3645b439ce8e7', scheme='https', host='service.io', tld='io', host_type='domain', path='/', query='q=3fc3645b439ce8e7')

