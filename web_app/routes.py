from flask import Flask, Blueprint, jsonify, request, render_template, current_app


sats = Blueprint("sats", __name__)

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