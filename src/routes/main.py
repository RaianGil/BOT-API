import flask
from flask import request, jsonify

def get():
    route_main = flask.Flask(__name__)
    route_main.config["DEBUG"] = True
    
    return route_main

def run():
    get().run()