from flask import Flask, Blueprint, jsonify, request, render_template, current_app
import requests
import lnurl
from lnurl import Lnurl, LnurlResponse, LnurlWithdrawResponse
from flask_migrate import Migrate
from web_app.models import User, db



# initialize to blueprint
sats = Blueprint("sats", __name__)


## LNURL TESTING

# encode
ln_url = lnurl.encode('https://service.io/?q=3fc3645b439ce8e7')
bech32 = ln_url.bech32  # "LNURL1DP68GURN8GHJ7UM9WFMXJCM99E5K7TELWY7NXENRXVMRGDTZXSENJCM98PJNWXQ96S9"
bech32_hrp = ln_url.bech32.hrp  # "lnurl"
url = ln_url.url  # "https://service.io/?q=3fc3645b439ce8e7"
host = ln_url.url.host  # "service.io"
base = ln_url.url.base  # "https://service.io/"
query = ln_url.url.query  # "q=3fc3645b439ce8e7"
query_params = ln_url.url.query_params  # {"q": "3fc3645b439ce8e7"}
#handle = ln_url.handle('lightning:LNURL1DP68GURN8GHJ7MRWW4EXCTNZD9NHXATW9EU8J730D3H82UNV94CXZ7FLWDJHXUMFDAHR6V33XCUNSVE38QV6UF')

# decode
ln_url_d = lnurl.decode(bech32)
ln_url_d_scheme = ln_url_d.scheme
ln_url_d_host = ln_url_d.host
ln_url_d_tld = ln_url_d.tld
ln_url_d_host_type = ln_url_d.host_type
ln_url_d_path = ln_url_d.path
ln_url_d_query = ln_url_d.query

# building your own LNURL responses example

res = LnurlWithdrawResponse(
    callback="https://lnurl.bigsun.xyz/lnurl-withdraw/callback/9702808",
    k1="38d304051c1b76dcd8c5ee17ee15ff0ebc02090c0afbc6c98100adfa3f920874",
    min_withdrawable=551000,
    max_withdrawable=551000,
    default_description="sample withdraw",
)
res_json = res.json()  # str
res_dict = res.dict()  # dict

# parsing (not working)

#lnurl = Lnurl('LNURL1DP68GURN8GHJ7MRWW4EXCTNZD9NHXATW9EU8J730D3H82UNV94MKJARGV3EXZAELWDJHXUMFDAHR6WFHXQERSVPCA649RV')
#lnurl_r = Lnurl(bech32)
#r = requests.get(lnurl_r.url)
#
#res = LnurlResponse.from_dict(r.json())  # LnurlPayResponse
#res_ok = res.ok  # bool
#res_max_send = res.max_sendable  # int
#res_max_sats = res.max_sats  # int
#res_base = res.callback.base  # str
#res_q_params = res.callback.query_params # dict
#res_meta1 = res.metadata  # str
#res_meta2 = res.metadata.list()  # list
#res_meta3 = res.metadata.text  # str
#res_image = res.metadata.images  # list


# index home page
# make it super simple
@sats.route("/", methods=['POST', 'GET'])
def index():
    return render_template('index.html')

@sats.route("/webln", methods=['POST', 'GET'])
def webln():
    return render_template('test.html')

@sats.route("/create_link", methods=['POST', 'GET'])
def create():
    return render_template('create_link.html')

# test payments
@sats.route("/pay", methods=['POST', 'GET'])
def pay():
    # get element by ID from pay page

    # pass in invoice, params, successAction, validatePreimage
        # wait for Lnurl.requestInvoice
            # set lnUrl0Address
            # token amount in sats
            # comment field

    # if statements
    
    return render_template('pay.html')

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
        db.session.add(User(ln_address=ln_address, link=link))
        #db.session.add(User(link=link))
        db.session.commit()
        message = jsonify({"message": "CREATED OK", "ln_address": ln_address, "embed link": link})
        error_message = jsonify({"message": "OOPS PLEASE SPECIFY A NAME!"})
        print(message)
        print(error_message)

        return render_template('wrapper.html')
    else:
        return render_template('error.html')


# testing

@sats.route("/test", methods=['POST', 'GET'])
def test():
    print("bech32: ", bech32)
    print("hrp: ", bech32_hrp)
    print("url: ", url)
    print("host: ", host)
    print("base: ", base)
    print("query: ", query)
    print("query params: ", query_params)
    
    #print("handle: ", handle)
    print("-- decode --")
    print("scheme: ", ln_url_d_scheme)
    print("host: ", ln_url_d_host)
    print("tld: ", ln_url_d_tld)
    print("host type: ", ln_url_d_host_type)
    print("path: ", ln_url_d_path)
    print("query: ", ln_url_d_query)

    # building our own json responses
    print("-- building LNURL json response")
    print("json: ", res_json)
    print("dict: ", res_dict)

    # parsing (not working)
    #print("-- parsing res --")
    #print("r: ", r)
    #print("res: ", res)
    #print("res ok: ", res_ok)
    #print("max send: ", res_max_send)
    #print("max sats: ", res_max_sats)
    #print("base: ", res_base)
    #print("query params: ", res_q_params)
    #print("metadata: ", res_meta1)
    #print("metadata2: ", res_meta2)
    #print("metadata3: ", res_meta3)
    #print("image: ", res_image)

    return render_template('test.html', ln_url=ln_url)

# examples
#>>> import lnurl
#>>> lnurl.encode('https://service.io/?q=3fc3645b439ce8e7')
#Lnurl('LNURL1DP68GURN8GHJ7UM9WFMXJCM99E5K7TELWY7NXENRXVMRGDTZXSENJCM98PJNWXQ96S9', bech32=Bech32('LNURL1DP68GURN8GHJ7UM9WFMXJCM99E5K7TELWY7NXENRXVMRGDTZXSENJCM98PJNWXQ96S9', hrp='lnurl', data=[13, 1, 26, 7, 8, 28, 3, 19, 7, 8, 23, 18, 30, 28, 27, 5, 14, 9, 27, 6, 18, 24, 27, 5, 5, 25, 20, 22, 30, 11, 25, 31, 14, 4, 30, 19, 6, 25, 19, 3, 6, 12, 27, 3, 8, 13, 11, 2, 6, 16, 25, 19, 18, 24, 27, 5, 7, 1, 18, 19, 14]), url=WebUrl('https://service.io/?q=3fc3645b439ce8e7', scheme='https', host='service.io', tld='io', host_type='domain', path='/', query='q=3fc3645b439ce8e7'))
#>>> lnurl.decode('LNURL1DP68GURN8GHJ7UM9WFMXJCM99E5K7TELWY7NXENRXVMRGDTZXSENJCM98PJNWXQ96S9')
#WebUrl('https://service.io/?q=3fc3645b439ce8e7', scheme='https', host='service.io', tld='io', host_type='domain', path='/', query='q=3fc3645b439ce8e7')