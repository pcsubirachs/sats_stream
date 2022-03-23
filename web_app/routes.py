from flask import Flask, Blueprint, jsonify, request, render_template, current_app


sats = Blueprint("sats", __name__)

# index home page
# make it super simple
@sats.route("/", methods=['POST', 'GET'])
def index():
    return render_template('index.html')
