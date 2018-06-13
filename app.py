from flask import Flask, jsonify, request
import requests

app = Flask(__name__)
api = "https://api.github.com"

@app.route('/api', methods=['GET'])
def getApi():
  r = requests.get(api)
  api_json = r.json()
  return jsonify(api_json)

@app.route('/api/<username>', methods=['GET'])
def getUser(username):
  user_endpoint = api+"/users/"+username
  user_requests = requests.get(user_endpoint)
  user_data = user_requests.json()
  return jsonify(user_data)

@app.route('/api/<username>/<section>', methods=['GET'])
def getUser(section):
  user_endpoint = api+"/users/"
  user_requests = r.get(user_endpoint)
  user_data = user_requests.json()
  return jsonify(user_data)

  
@app.route('/api/<username>', methods=['GET'])
def getUser(username):
  user_endpoint = api+"/users/"+username
  user_request = requests.get(user_endpoint)
  user_data = user_request.json()
  return jsonify(user_data)

@app.route('/api/<username>/<section>', methods=['GET'])
def getUser(section):
  user_endpoint = api+"/users/{}/{}".format(username,section)
  user_request = user_request.get(user_endpoint)
  user_data = user_request.json()
  return jsonify(user_data)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
