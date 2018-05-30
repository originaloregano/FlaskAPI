import os
# Using Flask since Python doesn't have built-in session management
from flask import Flask, session, render_template
# Our target library
import requests
import json

app = Flask(__name__)

# Generate a secret random key for the session
app.secret_key = os.urandom(24)

# Define routes for the examples to actually run
@app.route('/run_get')
def run_get():
	url = 'https://api.github.com/users/runnable'

	# this issues a GET to the url. replace "get" with "post", "head",
	# "put", "patch"... to make a request using a different method
	r = requests.get(url)

	return json.dumps(r.json(), indent=4)

@app.route('/run_post')
def run_post():
	url = 'http://httpbin.org/post'
	data = {'a': 10, 'b': [{'c': True, 'd': False}, None]}
	headers = {'Content-Type': 'application/json'}

	r = requests.post(url, data=json.dumps(data), headers=headers)

	return json.dumps(r.json(), indent=4)

# Define a route for the webserver
@app.route('/')
def index():
	return render_template('home.html')

if __name__ == '__main__':
	app.run(debug=True)
