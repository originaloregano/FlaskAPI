from flask import Flask, jsonify
from flask import make_response
from flask import request

app = Flask(__name__)
from methods import *
